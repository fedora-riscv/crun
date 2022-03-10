%global git0 https://github.com/containers/crun
  
%global built_tag 1.4.3
%global gen_version %(b=%{built_tag}; echo ${b/-/"~"})

Summary: OCI runtime written in C
Name: crun
Version: %{gen_version}
Release: %autorelease
URL: %{git0}
# Source0 generated using `make dist` in upstream repo
Source0: %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
License: GPLv2+

# We always run autogen.sh
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: python3
BuildRequires: libcap-devel
BuildRequires: systemd-devel
BuildRequires: yajl-devel
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: python3-libmount
BuildRequires: libtool
BuildRequires: go-md2man
BuildRequires: make
BuildRequires: glibc-static
BuildRequires: protobuf-c-devel
%ifnarch %ix86
BuildRequires: criu-devel >= 3.15
%endif
Provides: oci-runtime

%description
crun is a runtime for running OCI containers

%prep
%autosetup -p1 -n %{name}-%{version}

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
%autochangelog
