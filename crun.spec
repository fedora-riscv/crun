Name:           crun
Version:        0.1.1
Release:        1%{?dist}
Summary:        Lightweight, easy to use, simpler cron-like tool  

Group:          Applications/System
License:        GPLv2+
URL:            http://code.google.com/p/koolkit/wiki/crun
Source0:        http://koolkit.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
crun is a light weight, easy to use, simpler cron like tool.
It Executes a given program, a specified number of times, after a specified
time interval.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/crun

%changelog
* Fri Dec 11 2009 Damien Durand <splinux@fedoraproject.org> 0.1.1-1
- Initial release
