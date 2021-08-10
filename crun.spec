%global git0 https://github.com/containers/crun
  
# Used for comparing with latest upstream tag
# to decide whether to autobuild (non-rawhide only)
%global built_tag 0.21
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})

Summary: OCI runtime written in C
Name: crun
Version: 0.21
Release: 1%{?dist}
URL: %{git0}
# Source0 generated using `make dist` in upstream repo
Source0: %{name}-%{version}.tar.xz
License: GPLv2+

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
BuildRequires: make
BuildRequires: glibc-static
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
* Thu Aug 05 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.21-1
- bump to 0.21

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1.9-0.18.git60de767
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.20.1.9-0.17.git60de767
- bump to 0.20.1.9
- autobuilt 60de767

* Mon Jun 21 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.20.1.7-0.16.git7ef74c9
- bump to 0.20.1.7
- autobuilt 7ef74c9

* Sat Jun 19 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.19.1.13-0.15.git63400f2
- bump to 0.19.1.13
- autobuilt 63400f2

* Tue Jun 15 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.20.1.3-0.14.git9dec366
- bump to 0.20.1.3
- autobuilt 9dec366

* Thu Jun 10 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.20.1.1-0.13.git7adf4d0
- bump to 0.20.1.1
- autobuilt 7adf4d0

* Thu Jun 03 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.20.3-0.12.git8d6a8b5
- bump to 0.20.3
- autobuilt 8d6a8b5

* Wed Jun 02 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.20.1-0.11.gitffb75b2
- bump to 0.20.1
- autobuilt ffb75b2

* Tue May 25 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.19.1.50-0.10.git1942907
- bump to 0.19.1.50
- autobuilt 1942907

* Fri May 21 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.19.1.45-0.9.git4cc7fa1
- bump to 0.19.1.45
- autobuilt 4cc7fa1

* Sat May 15 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.19.1.41-0.8.gitf9c405d
- bump to 0.19.1.41
- autobuilt f9c405d

* Fri May 14 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.19.1.36-0.7.git2badd69
- bump to 0.19.1.36
- autobuilt 2badd69

* Thu May 13 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.19.1.31-0.6.gitb83eda7
- bump to 0.19.1.31
- autobuilt b83eda7

* Tue May 11 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.19.1.26-0.5.git029e0ed
- bump to 0.19.1.26
- autobuilt 029e0ed

* Mon May 10 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.19.1.22-0.4.git4e968c9
- bump to 0.19.1.22
- autobuilt 4e968c9

* Sat May 08 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.19.1.19-0.3.gitb6c3139
- bump to 0.19.1.19
- autobuilt b6c3139

* Fri May 07 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.19.1.17-0.2.git3f6a944
- bump to 0.19.1.17
- autobuilt 3f6a944

* Mon May 03 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.19.1.11-0.1.git1dead7e
- built 1dead7e

* Wed Apr 28 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.19.1.7-0.1.git3886321
- built 3886321

* Thu Apr 22 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.19.1-2
- rebuild for new bodhi

* Thu Apr 22 2021 Giuseppe Scrivano <gscrivan@redhat.com> - 0.19.1-1
- built version 0.19.1

* Tue Apr 13 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.19-2
- unversioned Provides: oci-runtime
- runc package will also provide an unversioned Provides: oci-runtime.
- user should pull in runc separately or else it will install crun by default
 (alphabetical order)
- similar situation as caddy, httpd, lighttpd and nginx having Provides:
webserver

* Tue Apr 06 2021 Giuseppe Scrivano <gscrivan@redhat.com> - 0.19-1
- built version 0.19

* Wed Mar 31 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.18-5
- linux: always remount bind mounts ghpr#640

* Thu Mar 25 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.18-4
- bump release tag to stay ahead of older fedora

* Thu Mar 25 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.18-2
- Requires: libcap >= 2.48

* Fri Feb 19 2021 Giuseppe Scrivano <gscrivan@redhat.com> - 0.18-1
- built version 0.18

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Giuseppe Scrivano <gscrivan@redhat.com> - 0.17-1
- built version 0.17

* Thu Dec 17 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.16-3
- build with CRIU

* Wed Nov 25 2020 Jindrich Novy <jnovy@redhat.com> - 0.16-2
- fix license

* Tue Nov 24 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.16-1
- built version 0.16

* Wed Nov 04 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.15.1-1
- built version 0.15.1

* Wed Sep 30 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.15-5
- rebuild to bump release tag ahead of older fedoras

* Wed Sep 30 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.15-3
- backport "exec: check read bytes from sync"

* Wed Sep 23 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.15-2
- rebuild

* Wed Sep 23 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.15-1
- build version 0.15

* Mon Sep 14 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.14.1-5
- backport 4453af4c060e380051552ee589af5cad37f2ae82

* Mon Aug 31 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.14.1-4
- rebuild

* Thu Aug 27 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.14.1-3
- backport ed9c3e6f466dfb6d2e79802060fabd5f4b66f78e

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.14.1-1
- built version 0.14.1

* Thu Jul 02 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.14-1
- built version 0.14

* Wed Apr 15 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.13-2
- release bump for correct upgrade path

* Thu Mar 05 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.13-1
- built version 0.13

* Mon Feb 17 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.12.2.1-1
- built version 0.12.2.1

* Mon Feb 17 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.12.2-1
- built version 0.12.2

* Thu Feb 6 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.12.1-1
- built version 0.12.1

* Mon Feb 3 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.12-1
- built version 0.12

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.11-1
- built version 0.11

* Mon Nov 18 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.6-1
- built version 0.10.6

* Sun Nov 10 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.5-2
- built version 0.10.5
- fix CVE-2019-18837

* Sun Nov 10 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.5-1
- built version 0.10.5

* Thu Oct 31 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.4-1
- built version 0.10.4

* Tue Oct 29 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.3-1
- built version 0.10.3

* Mon Oct 7 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.2-1
- built version 0.10.2

* Fri Oct 4 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.1-1
- built version 0.10.1

* Tue Oct 1 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10-1
- built version 0.10

* Fri Sep 13 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.9.1-1
- built version 0.9.1

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
