%if 0%{?fedora} >= 37
%ifarch aarch64,x86_64
%global krun_support enabled
%endif
%else
%global krun_support disabled
%endif

%global built_tag 1.5

Summary: OCI runtime written in C
Name: crun
Version: 1.5
URL: https://github.com/containers/%{name}
Source0: %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
%if "%{_vendor}" == "debbuild"
Packager: Lokesh Mandvekar <lsm5@fedoraproject.org>
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
%if "%{krun_support}" == "enabled"
BuildRequires: libkrun-devel
Provides: krun
%endif
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: python3-libmount
BuildRequires: make
BuildRequires: glibc-static
BuildRequires: protobuf-c-devel
%ifnarch %ix86
BuildRequires: criu-devel >= 3.17.1-2
%endif
%endif
Requires: criu >= 3.17.1-2
Provides: oci-runtime

%description
%{name} is a runtime for running OCI containers

%prep
%autosetup -Sgit

%build
./autogen.sh

%if "%{krun_support}" == "enabled"
%configure --disable-silent-rules --with-libkrun
%else
%configure --disable-silent-rules
%endif

%make_build

%install
%make_install
rm -rf %{buildroot}%{_prefix}/lib*

%if "%{krun_support}" == "enabled"
ln -s %{_bindir}/%{name} %{buildroot}%{_bindir}/krun
%endif

%files
%license COPYING
%{_bindir}/%{name}
%if "%{krun_support}" == "enabled"
%{_bindir}/krun
%endif
%{_mandir}/man1/*

%changelog
%if "%{_vendor}" != "debbuild"
%autochangelog
%endif
