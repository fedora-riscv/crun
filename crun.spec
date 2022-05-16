%global built_tag 1.4.5

Summary: OCI runtime written in C
Name: crun
Version: 1.4.5
URL: https://github.com/containers/%{name}
Source0: %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
%if "%{_vendor}" == "debbuild"
Maintainer: Lokesh Mandvekar <https://github.com/lsm5>
License: GPL-2.0+
Release: 0%{?dist}
%else
License: GPLv2+
Release: %autorelease
%endif
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: go-md2man
BuildRequires: libtool
%if "%{_vendor}" == "debbuild"
BuildRequires: git
BuildRequires: libcap-dev
BuildRequires: libseccomp-dev
BuildRequires: libsystemd-dev
BuildRequires: libyajl-dev
BuildRequires: pkg-config
%else
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: python3
BuildRequires: libcap-devel
BuildRequires: systemd-devel
BuildRequires: yajl-devel
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: python3-libmount
BuildRequires: make
BuildRequires: glibc-static
BuildRequires: protobuf-c-devel
%ifnarch %ix86
BuildRequires: criu-devel >= 3.15
%endif
%endif
Provides: oci-runtime

%description
%{name} is a runtime for running OCI containers

%prep
%autosetup -Sgit

%build
./autogen.sh
%configure --disable-silent-rules

%make_build

%install
%make_install
rm -rf %{buildroot}%{_prefix}/lib*

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
%if "%{_vendor}" != "debbuild"
%autochangelog
%endif
