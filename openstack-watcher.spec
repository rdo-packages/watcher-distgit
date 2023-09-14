%global milestone .0rc1
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x815AFEC729392386480E076DCC0DFE2D21C023C9
%global service watcher
%global common_desc Watcher is an Infrastructure Optimization service.
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order bashate os-api-ref
# Exclude sphinx from BRs if docs are disabled
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif

%global with_doc 1

Name:           openstack-%{service}
Version:        11.0.0
Release:        0.1%{?milestone}%{?dist}
Summary:        Openstack Infrastructure Optimization service.
License:        Apache-2.0
URL:            https://launchpad.net/watcher
Source0:        https://tarballs.openstack.org/%{service}/python-%{service}-%{upstream_version}.tar.gz

#
# patches_base=11.0.0.0rc1
#

# Systemd scripts
Source10:       openstack-watcher-api.service
Source11:       openstack-watcher-applier.service
Source12:       openstack-watcher-decision-engine.service
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{service}/python-%{service}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  systemd

%description
%{common_desc}

%package -n     python3-%{service}
Summary:        Watcher Python libraries

%description -n python3-%{service}
Watcher provides a flexible and scalable resource optimization service for
multi-tenant OpenStack-based clouds. Watcher provides a complete optimization
loop—including everything from a metrics receiver, complex event processor
and profiler, optimization processor and an action plan applier. This provides
a robust framework to realize a wide range of cloud optimization goals,
including the reduction of data center operating costs, increased system
performance via intelligent virtual machine migration, increased energy
efficiency—and more!

This package contains the Python libraries.

%package common

Summary: Components common for OpenStack Watcher

Requires: python3-%{service} = %{version}-%{release}

%{?systemd_ordering}

%description common
Watcher provides a flexible and scalable resource optimization service
for multi-tenant OpenStack-based clouds. Watcher provides a complete
optimization loop—including everything from a metrics receiver, complex
event processor and profiler, optimization processor and an action
plan applier. This provides a robust framework to realize a wide range of
cloud optimization goals, including the reduction of data center
operating costs, increased system performance via intelligent virtual
machine migration, increased energy efficiency—and more!

This package contains the common files.

%package api

Summary:     OpenStack Watcher API service
Requires:    %{name}-common = %{version}-%{release}

%description api
%{common_desc}

This package contains the ReST API.

%package applier
Summary:     OpenStack Watcher Applier service
Requires:    %{name}-common = %{version}-%{release}

%description applier
%{common_desc}

This package contains the watcher applier, which is one of core services of
watcher.

%package     decision-engine
Summary:     OpenStack Watcher Decision Engine service
Requires:    %{name}-common = %{version}-%{release}

%description decision-engine
%{common_desc}

This package contains the Watcher Decision Engine, which is one of core
services of watcher.

%package -n     python3-%{service}-tests-unit
Summary:        Watcher unit tests
Requires:       %{name}-common = %{version}-%{release}

%description -n python3-watcher-tests-unit
This package contains the Watcher test files.

%if 0%{?with_doc}
%package        doc
Summary:        Documentation for OpenStack Workflow Service

BuildRequires:  python3-sphinxcontrib-rsvgconverter


%description    doc
OpenStack Watcher documentaion.

This package contains the documentation
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python-%{service}-%{upstream_version} -S git


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

# Automatic BR generation
%generate_buildrequires
%if 0%{?with_doc}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

%install
%pyproject_install
PYTHONPATH="%{buildroot}/%{python3_sitelib}" oslo-config-generator --config-file etc/watcher/oslo-config-generator/watcher.conf  \
                      --output-file etc/watcher.conf.sample
# The automatic value of pybasedir is wrong and unneeded and makes build to fail
sed -i "/#pybasedir.*/d" etc/watcher.conf.sample

%if 0%{?with_doc}
%tox -e docs
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

mkdir -p %{buildroot}%{_sysconfdir}/watcher/
mkdir -p %{buildroot}%{_localstatedir}/log/watcher
mkdir -p %{buildroot}%{_localstatedir}/run/watcher
mkdir -p %{buildroot}%{_localstatedir}/cache/watcher

install -p -D -m 644 %SOURCE10 %{buildroot}%{_unitdir}/openstack-watcher-api.service
install -p -D -m 644 %SOURCE11 %{buildroot}%{_unitdir}/openstack-watcher-applier.service
install -p -D -m 644 %SOURCE12 %{buildroot}%{_unitdir}/openstack-watcher-decision-engine.service

install -p -D -m 640 etc/watcher.conf.sample \
                     %{buildroot}%{_sysconfdir}/watcher/watcher.conf
chmod +x %{buildroot}%{_bindir}/watcher*

# Remove unneeded in production
rm -f %{buildroot}/usr/etc/watcher.conf.sample
rm -f %{buildroot}/usr/etc/watcher/README-watcher.conf.txt
rm -rf %{buildroot}/usr/etc/watcher/oslo-config-generator

# Move /usr/etc/watcher to /etc/watcher
rm -rf %{buildroot}/usr/etc

%pre common
USERNAME=watcher
GROUPNAME=$USERNAME
HOMEDIR=%{_localstatedir}/cache/$USERNAME
getent group $GROUPNAME >/dev/null || groupadd -r $GROUPNAME
getent passwd $USERNAME >/dev/null ||
    useradd -r -g $GROUPNAME -G $GROUPNAME -d $HOMEDIR -s /sbin/nologin \
            -c "Satcher Services" $USERNAME
exit 0

%post api
%systemd_post openstack-watcher-api.service
%preun api
%systemd_preun openstack-watcher-api.service
%postun api
%systemd_postun_with_restart openstack-watcher-api.service

%post applier
%systemd_post openstack-watcher-applier.service
%preun applier
%systemd_preun openstack-watcher-applier.service
%postun applier
%systemd_postun_with_restart openstack-watcher-applier.service

%post decision-engine
%systemd_post openstack-watcher-decision-engine.service
%preun decision-engine
%systemd_preun openstack-watcher-decision-engine.service
%postun decision-engine
%systemd_postun_with_restart openstack-watcher-decision-engine.service

%files api
%license LICENSE
%{_bindir}/watcher-api
%{_bindir}/watcher-api-wsgi
%{_unitdir}/openstack-watcher-api.service

%files common
%license LICENSE
%dir %{_sysconfdir}/watcher
%config(noreplace) %attr(-, watcher, watcher) %{_sysconfdir}/watcher/*
%{_bindir}/watcher-db-manage
%dir %attr(755, watcher, watcher) %{_localstatedir}/run/watcher
%dir %attr(750, watcher, root) %{_localstatedir}/log/watcher
%dir %attr(755, watcher, watcher) %{_localstatedir}/cache/watcher
%{_bindir}/watcher-sync
%{_bindir}/watcher-status

%if 0%{?with_doc}
%files doc
%license LICENSE
%doc doc/build/html
%endif

%files applier
%license LICENSE
%{_bindir}/watcher-applier
%{_unitdir}/openstack-watcher-applier.service

%files decision-engine
%license LICENSE
%{_bindir}/watcher-decision-engine
%{_unitdir}/openstack-watcher-decision-engine.service


%files -n python3-%{service}
%license LICENSE
%{python3_sitelib}/%{service}
%{python3_sitelib}/python_%{service}-*.dist-info
%exclude %{python3_sitelib}/%{service}/tests

%files -n python3-%{service}-tests-unit
%license LICENSE
%{python3_sitelib}/%{service}/tests

%changelog
* Thu Sep 14 2023 RDO <dev@lists.rdoproject.org> 11.0.0-0.1.0rc1
- Update to 11.0.0.0rc1

