# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%global service watcher
%global common_desc Watcher is an Infrastructure Optimization service.
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1

Name:           openstack-%{service}
Version:        XXX
Release:        XXX
Summary:        Openstack Infrastructure Optimization service.
License:        ASL 2.0
URL:            https://launchpad.net/watcher
Source0:        https://tarballs.openstack.org/%{service}/python-%{service}-%{upstream_version}.tar.gz

# Systemd scripts
Source10:       openstack-watcher-api.service
Source11:       openstack-watcher-applier.service
Source12:       openstack-watcher-decision-engine.service

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-oslo-config >= 2:5.2.0
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr >= 3.1.1
BuildRequires:  systemd
BuildRequires:  python%{pyver}-debtcollector
BuildRequires:  python-debtcollector-doc
BuildRequires:  python%{pyver}-APScheduler
BuildRequires:  python%{pyver}-microversion-parse


%description
%{common_desc}

%package -n     python%{pyver}-%{service}
Summary:        Watcher Python libraries
%{?python_provide:%python_provide python%{pyver}-%{service}}

Requires:       python%{pyver}-APScheduler
Requires:       python%{pyver}-croniter >= 0.3.19
Requires:       python%{pyver}-jsonpatch >= 1.21
Requires:       python%{pyver}-jsonschema >= 2.6.0
Requires:       python%{pyver}-keystoneauth1 >= 3.4.0
Requires:       python%{pyver}-keystonemiddleware >= 4.21.0
Requires:       python%{pyver}-oslo-concurrency >= 3.26.0
Requires:       python%{pyver}-oslo-cache >= 1.29.0
Requires:       python%{pyver}-oslo-config >= 2:5.2.0
Requires:       python%{pyver}-oslo-context >= 2.20.0
Requires:       python%{pyver}-oslo-db >= 4.35.0
Requires:       python%{pyver}-oslo-i18n >= 3.20.0
Requires:       python%{pyver}-oslo-log >= 3.37.0
Requires:       python%{pyver}-oslo-messaging >= 5.36.0
Requires:       python%{pyver}-oslo-policy >= 1.34.0
Requires:       python%{pyver}-oslo-reports >= 1.27.0
Requires:       python%{pyver}-oslo-serialization >= 2.25.0
Requires:       python%{pyver}-oslo-service >= 1.30.0
Requires:       python%{pyver}-oslo-upgradecheck >= 0.1.0
Requires:       python%{pyver}-oslo-utils >= 3.36.0
Requires:       python%{pyver}-oslo-versionedobjects >= 1.32.0
Requires:       python%{pyver}-pbr >= 3.1.1
Requires:       python%{pyver}-pecan >= 1.2.1
Requires:       python%{pyver}-prettytable >= 0.7.2
Requires:       python%{pyver}-voluptuous
Requires:       python%{pyver}-ceilometerclient >= 2.9.0
Requires:       python%{pyver}-cinderclient >= 3.5.0
Requires:       python%{pyver}-glanceclient >= 1:2.9.1
Requires:       python%{pyver}-gnocchiclient >= 7.0.1
Requires:       python%{pyver}-ironicclient >= 2.3.0
Requires:       python%{pyver}-keystoneclient >= 3.15.0
Requires:       python%{pyver}-microversion-parse >= 0.2.1
Requires:       python%{pyver}-monascaclient >= 1.12.0
Requires:       python%{pyver}-neutronclient >= 6.7.0
Requires:       python%{pyver}-novaclient >= 1:10.1.0
Requires:       python%{pyver}-openstackclient >= 3.14.0
Requires:       python%{pyver}-six >= 1.11.0
Requires:       python%{pyver}-sqlalchemy >= 1.2.5
Requires:       python%{pyver}-stevedore >= 1.28.0
Requires:       python%{pyver}-taskflow >= 3.1.0
Requires:       python%{pyver}-webob >= 1.7.4
Requires:       python%{pyver}-wsme >= 0.9.2

# Handle python2 exception
%if %{pyver} == 2
Requires:       python-enum34
Requires:       python-lxml >= 3.2.1
Requires:       python-networkx >= 1.10
Requires:       python-paste-deploy >= 1.5.2
%else
Requires:       python%{pyver}-lxml >= 3.2.1
Requires:       python%{pyver}-networkx >= 1.10
Requires:       python%{pyver}-paste-deploy >= 1.5.2
%endif

%description -n python%{pyver}-%{service}
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

Requires: python%{pyver}-%{service} = %{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif

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

%package -n     python%{pyver}-%{service}-tests-unit
Summary:        Watcher unit tests
%{?python_provide:%python_provide python%{pyver}-%{service}-tests-unit}
Requires:       %{name}-common = %{version}-%{release}

%description -n python%{pyver}-watcher-tests-unit
This package contains the Watcher test files.

%if 0%{?with_doc}
%package        doc
Summary:        Documentation for OpenStack Workflow Service

BuildRequires:  python%{pyver}-hacking
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-oslotest
BuildRequires:  python%{pyver}-oslo-db
BuildRequires:  python%{pyver}-oslo-cache
BuildRequires:  python%{pyver}-croniter
BuildRequires:  python%{pyver}-jsonschema
BuildRequires:  python%{pyver}-os-testr
BuildRequires:  python%{pyver}-pecan
BuildRequires:  python%{pyver}-subunit
BuildRequires:  python%{pyver}-cinderclient
BuildRequires:  python%{pyver}-glanceclient
BuildRequires:  python%{pyver}-keystoneclient
BuildRequires:  python%{pyver}-novaclient
BuildRequires:  python%{pyver}-monascaclient
BuildRequires:  python%{pyver}-gnocchiclient
BuildRequires:  python%{pyver}-keystonemiddleware
BuildRequires:  python%{pyver}-ceilometerclient
BuildRequires:  python%{pyver}-ironicclient
BuildRequires:  python%{pyver}-openstackclient
BuildRequires:  python%{pyver}-testrepository
BuildRequires:  python%{pyver}-testscenarios
BuildRequires:  python%{pyver}-testtools
BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-openstackdocstheme
BuildRequires:  python%{pyver}-sphinxcontrib-apidoc
BuildRequires:  python%{pyver}-sphinxcontrib-pecanwsme
BuildRequires:  python%{pyver}-oslo-log
BuildRequires:  python%{pyver}-oslo-policy
BuildRequires:  python%{pyver}-oslo-versionedobjects
BuildRequires:  python%{pyver}-oslo-messaging
BuildRequires:  python%{pyver}-oslo-reports
BuildRequires:  python%{pyver}-reno
BuildRequires:  python%{pyver}-jsonpatch
BuildRequires:  python%{pyver}-taskflow
BuildRequires:  python%{pyver}-wsme
BuildRequires:  python%{pyver}-voluptuous
BuildRequires:  python%{pyver}-debtcollector
BuildRequires:  openstack-macros

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-freezegun
BuildRequires:  python-networkx
BuildRequires:  python-sphinxcontrib-httpdomain
%else
BuildRequires:  python%{pyver}-freezegun
BuildRequires:  python%{pyver}-networkx
BuildRequires:  python%{pyver}-sphinxcontrib-httpdomain
%endif


%description    doc
OpenStack Watcher documentaion.

This package contains the documentation
%endif


%prep
%autosetup -n python-%{service}-%{upstream_version} -S git

%py_req_cleanup

%build
%{pyver_build}
oslo-config-generator-%{pyver} --config-file etc/watcher/oslo-config-generator/watcher.conf  \
                      --output-file etc/watcher.conf.sample

%install
%{pyver_install}

%if 0%{?with_doc}
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build-%{pyver} -b html doc/source doc/build/html
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
HOMEDIR=/home/$USERNAME
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


%files -n python%{pyver}-%{service}
%license LICENSE
%{pyver_sitelib}/%{service}
%{pyver_sitelib}/python_%{service}-*.egg-info
%exclude %{pyver_sitelib}/%{service}/tests

%files -n python%{pyver}-%{service}-tests-unit
%license LICENSE
%{pyver_sitelib}/%{service}/tests

%changelog
