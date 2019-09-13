%global git0 https://github.com/containers/%{name}
%global commit0 6a2c11176300e86a99226d77777e1556d98f0416
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: OCI runtime written in C
Name: crun
Version: 0.9
Release: 2%{?dist}
Source0: %{git0}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
License: GPLv3+
URL: https://github.com/containers/crun

# We always run autogen.sh
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: python
BuildRequires: git
BuildRequires: libcap-devel
BuildRequires: systemd-devel
BuildRequires: yajl-devel
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: python3-libmount
BuildRequires: libtool
BuildRequires: go-md2man
Provides: oci-runtime = 2

%description
crun is a runtime for running OCI containers

%prep
%autosetup -Sgit -n %{name}-%{commit0}

%build
./autogen.sh
%configure --disable-silent-rules

%make_build

%install
%make_install
rm -rf $RPM_BUILD_ROOT/usr/lib*

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Fri Sep 13 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.9-2
- built version 6a2c11176300e86a99226d77777e1556d98f0416

* Wed Sep 11 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.9-1
- built version 0.9

* Tue Sep 10 2019 Jindrich Novy <jnovy@redhat.com> - 0.8-3
- Add versioned oci-runtime provide.

* Mon Sep 9 2019 Dan Walsh <dwalsh@redhat.com> - 0.8-2
- Add provides oci-runtime

* Mon Aug 19 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.8-1
- built version 0.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.7-1
- built version 0.7

* Tue Jun 18 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.6-1
- built version 0.6
