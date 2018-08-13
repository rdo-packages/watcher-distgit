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
BuildRequires:  python2-devel
BuildRequires:  python2-oslo-config >= 2:5.2.0
BuildRequires:  python2-setuptools
BuildRequires:  python2-pbr >= 3.1.1
BuildRequires:  systemd
BuildRequires:  python2-debtcollector
BuildRequires:  python-debtcollector-doc
BuildRequires:  python2-APScheduler

%description
%{common_desc}

%package -n     python-%{service}
Summary:        Watcher Python libraries

Requires:       python2-APScheduler
Requires:       python-enum34
Requires:       python2-croniter >= 0.3.20
Requires:       python2-jsonpatch >= 1.21
Requires:       python2-jsonschema >= 2.6.0
Requires:       python2-keystoneauth1 >= 3.4.0
Requires:       python2-keystonemiddleware >= 4.21.0
Requires:       python-lxml >= 3.2.1
Requires:       python-networkx >= 1.11
Requires:       python2-oslo-concurrency >= 3.26.0
Requires:       python2-oslo-cache >= 1.29.0
Requires:       python2-oslo-config >= 2:5.2.0
Requires:       python2-oslo-context >= 2.20.0
Requires:       python2-oslo-db >= 4.35.0
Requires:       python2-oslo-i18n >= 3.20.0
Requires:       python2-oslo-log >= 3.37.0
Requires:       python2-oslo-messaging >= 5.36.0
Requires:       python2-oslo-policy >= 1.34.0
Requires:       python2-oslo-reports >= 1.27.0
Requires:       python2-oslo-serialization >= 2.25.0
Requires:       python2-oslo-service >= 1.30.0
Requires:       python2-oslo-utils >= 3.36.0
Requires:       python2-oslo-versionedobjects >= 1.32.0
Requires:       python-paste-deploy >= 1.5.2
Requires:       python2-pbr >= 3.1.1
Requires:       python2-pecan >= 1.2.1
Requires:       python2-prettytable >= 0.7.2
Requires:       python2-voluptuous
Requires:       python2-ceilometerclient >= 2.9.0
Requires:       python2-cinderclient >= 3.5.0
Requires:       python2-glanceclient >= 1:2.9.1
Requires:       python2-gnocchiclient >= 7.0.1
Requires:       python2-ironicclient >= 2.3.0
Requires:       python2-keystoneclient >= 3.15.0
Requires:       python2-monascaclient >= 1.12.0
Requires:       python2-neutronclient >= 6.7.0
Requires:       python2-novaclient >= 1:10.1.0
Requires:       python2-openstackclient >= 3.14.0
Requires:       python2-six >= 1.11.0
Requires:       python2-sqlalchemy >= 1.2.5
Requires:       python2-stevedore >= 1.28.0
Requires:       python2-taskflow >= 3.1.0
Requires:       python-webob >= 1.7.4
Requires:       python2-wsme >= 0.9.2

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
%{?systemd_requires}

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
BuildRequires:  python2-hacking
BuildRequires:  python2-mock
BuildRequires:  python2-oslotest
BuildRequires:  python2-oslo-db
BuildRequires:  python2-oslo-cache
BuildRequires:  python2-croniter
BuildRequires:  python2-jsonschema
BuildRequires:  python2-os-testr
BuildRequires:  python2-pecan
BuildRequires:  python2-subunit
BuildRequires:  python-networkx
BuildRequires:  python2-cinderclient
BuildRequires:  python2-glanceclient
BuildRequires:  python2-keystoneclient
BuildRequires:  python2-novaclient
BuildRequires:  python2-monascaclient
BuildRequires:  python2-gnocchiclient
BuildRequires:  python2-keystonemiddleware
BuildRequires:  python2-ceilometerclient
BuildRequires:  python2-ironicclient
BuildRequires:  python2-openstackclient
BuildRequires:  python2-testrepository
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python2-sphinx
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python-sphinxcontrib-httpdomain
BuildRequires:  python2-sphinxcontrib-pecanwsme
BuildRequires:  python2-oslo-log
BuildRequires:  python2-oslo-policy
BuildRequires:  python2-oslo-versionedobjects
BuildRequires:  python2-oslo-messaging
BuildRequires:  python2-oslo-reports
BuildRequires:  python2-reno
BuildRequires:  python2-jsonpatch
BuildRequires:  python2-taskflow
BuildRequires:  python2-wsme
BuildRequires:  python2-voluptuous
BuildRequires:  python2-debtcollector
BuildRequires:  openstack-macros


%description    doc
OpenStack Watcher documentaion.

This package contains the documentation
%endif


%prep
%autosetup -n python-%{service}-%{upstream_version} -S git

%py_req_cleanup

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
