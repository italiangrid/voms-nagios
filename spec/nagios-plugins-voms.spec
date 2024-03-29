Name: nagios-plugins-voms
Version: 1.0.0
Release: 1%{?dist}
Summary: The VOMS service nagios probes

Group: Applications/Internet
License: ASL 2.0
URL: https://wiki.italiangrid.org/twiki/bin/view/VOMS
Source: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Packager: Andrea Ceccanti <andrea.ceccanti@cnaf.infn.it>

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides the Nagios probes for the VOMS Admin service.

%prep
%setup -c

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/grid-monitoring/probes/%{name}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

install -m 755 src/voms-admin-probe $RPM_BUILD_ROOT%{_libexecdir}/grid-monitoring/probes/%{name}
install -m 644 README.md $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%{_libexecdir}/grid-monitoring/probes/%{name}
%{_docdir}/%{name}-%{version}

%changelog

* Thu Dec 15 2011 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.0-1
- First packaging
