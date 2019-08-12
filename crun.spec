Summary: OCI runtime written in C
Name: crun
Version: 0.7
Release: 2%{?dist}
Source0: https://github.com/containers/crun/releases/download/%{version}/%{name}-%{version}.tar.gz
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

%description
crun is a runtime for running OCI containers

%prep
%autosetup -n %{name}-%{version}

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
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.7-1
- built version 0.7

* Tue Jun 18 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.6-1
- built version 0.6
