Summary: OCI runtime written in C
Name: crun
Version: 0.6
Release: 1%{?dist}
Source0: https://github.com/giuseppe/crun/releases/download/%{version}/%{name}-%{version}.tar.gz
License: GPLv3+
URL: https://github.com/giuseppe/crun

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
crun is a OCI runtime

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
* Tue Jun 18 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.6-1
- built version 0.6
