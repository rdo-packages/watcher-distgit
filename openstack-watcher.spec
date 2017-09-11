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
BuildRequires:  python-devel
BuildRequires:  python-oslo-config >= 2:4.0.0
BuildRequires:  python-setuptools
BuildRequires:  python-pbr >= 2.0.0
BuildRequires:  systemd
BuildRequires:  python-debtcollector
BuildRequires:  python-debtcollector-doc
BuildRequires:  python-APScheduler

%description
%{common_desc}

%package -n     python-%{service}
Summary:        Watcher Python libraries

Requires:       python-APScheduler
Requires:       python-enum34
Requires:       python-croniter >= 0.3.4
Requires:       python-jsonpatch >= 1.1
Requires:       python-jsonschema >= 2.0.0
Requires:       python-keystoneauth1 >= 3.1.0
Requires:       python-keystonemiddleware >= 4.12.0
Requires:       python-lxml >= 2.3
Requires:       python-networkx >= 1.10
Requires:       python-oslo-concurrency >= 3.8.0
Requires:       python-oslo-cache >= 1.5.0
Requires:       python-oslo-config >= 2:4.0.0
Requires:       python-oslo-context >= 2.14.0
Requires:       python-oslo-db >= 4.24.0
Requires:       python-oslo-i18n >= 2.1.0
Requires:       python-oslo-log >= 3.22.0
Requires:       python-oslo-messaging >= 5.24.2
Requires:       python-oslo-policy >= 1.23.0
Requires:       python-oslo-reports >= 0.6.0
Requires:       python-oslo-serialization >= 1.10.0
Requires:       python-oslo-service >= 1.10.0
Requires:       python-oslo-utils >= 3.20.0
Requires:       python-oslo-versionedobjects >= 1.17.0
Requires:       python-paste-deploy >= 1.5.0
Requires:       python-pbr >= 2.0.0
Requires:       python-pecan >= 1.0.0
Requires:       python-prettytable >= 0.7.1
Requires:       python-voluptuous
Requires:       python-ceilometerclient >= 2.5.0
Requires:       python-cinderclient >= 3.1.0
Requires:       python-glanceclient >= 1:2.8.0
Requires:       python-gnocchiclient >= 2.7.0
Requires:       python-ironicclient >= 1.14.0
Requires:       python-keystoneclient >= 1:3.8.0
Requires:       python-monascaclient >= 1.7.0
Requires:       python-neutronclient >= 6.3.0
Requires:       python-novaclient >= 1:9.0.0
Requires:       python-openstackclient >= 3.3.0
Requires:       python-six >= 1.9.0
Requires:       python-sqlalchemy >= 1.0.10
Requires:       python-stevedore >= 1.20.0
Requires:       python-taskflow >= 2.7.0
Requires:       python-webob >= 1.7.1
Requires:       python-wsme >= 0.8
Requires:       python-setuptools

%description -n python-%{service}
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

Requires: python-%{service} = %{version}-%{release}
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

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

%package -n     python-%{service}-tests-unit
Summary:        Watcher unit tests
Requires:       %{name}-common = %{version}-%{release}

%description -n python-watcher-tests-unit
This package contains the Watcher test files.

%if 0%{?with_doc}
%package        doc
Summary:        Documentation for OpenStack Workflow Service

BuildRequires:  python-freezegun
BuildRequires:  python-hacking
BuildRequires:  python-mock
BuildRequires:  python-oslotest
BuildRequires:  python-oslo-db
BuildRequires:  python-oslo-cache
BuildRequires:  python-croniter
BuildRequires:  python-jsonschema
BuildRequires:  python-os-testr
BuildRequires:  python-pecan
BuildRequires:  python-subunit
BuildRequires:  python-networkx
BuildRequires:  python-cinderclient
BuildRequires:  python-glanceclient
BuildRequires:  python-keystoneclient
BuildRequires:  python-novaclient
BuildRequires:  python-monascaclient
BuildRequires:  python-gnocchiclient
BuildRequires:  python-keystonemiddleware
BuildRequires:  python-ceilometerclient
BuildRequires:  python-ironicclient
BuildRequires:  python-openstackclient
BuildRequires:  python-testrepository
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
BuildRequires:  python-sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-sphinxcontrib-httpdomain
BuildRequires:  python-sphinxcontrib-pecanwsme
BuildRequires:  python-oslo-log
BuildRequires:  python-oslo-policy
BuildRequires:  python-oslo-versionedobjects
BuildRequires:  python-oslo-messaging
BuildRequires:  python-oslo-reports
BuildRequires:  python-reno
BuildRequires:  python-jsonpatch
BuildRequires:  python-taskflow
BuildRequires:  python-wsme
BuildRequires:  python-voluptuous
BuildRequires:  python-debtcollector
BuildRequires:  bandit


%description    doc
OpenStack Watcher documentaion.

This package contains the documentation
%endif


%prep
%autosetup -n python-%{service}-%{upstream_version} -S git

rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%{__python2} setup.py build
oslo-config-generator --config-file etc/watcher/oslo-config-generator/watcher.conf  \
                      --output-file etc/watcher.conf.sample

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{?with_doc}
export PYTHONPATH="$( pwd ):$PYTHONPATH"
%{__python2} setup.py build_sphinx -b html
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
mv %{buildroot}/usr/etc/watcher/policy.json %{buildroot}/etc/watcher/policy.json
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


%files -n python-%{service}
%license LICENSE
%{python2_sitelib}/%{service}
%{python2_sitelib}/python_%{service}-*.egg-info
%exclude %{python2_sitelib}/%{service}/tests

%files -n python-%{service}-tests-unit
%license LICENSE
%{python2_sitelib}/%{service}/tests

%changelog
