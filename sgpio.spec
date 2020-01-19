Summary: SGPIO captive backplane tool
Name: sgpio
Version: 1.2.0.10
Release: 11%{?dist}
License: GPLv2+
Group: System Environment/Base
URL: http://sources.redhat.com/lvm2/wiki/DMRAID_Eventing
Source: sgpio-1.2-0.10-src.tar.gz
# there is no official download link for the latest package
#Source: http://sources.redhat.com/lvm2/wiki/DMRAID_Eventing?action=AttachFile&do=get&target=sgpio-1.2.tgz
Patch0: sgpio-1.2-makefile.patch
Patch1: sgpio-1.2-coverity.patch
BuildRequires: dos2unix

%description
Intel SGPIO enclosure management utility

%prep
%setup -q -n sgpio
dos2unix --keepdate Makefile README
%patch0 -p1 -b .makefile
%patch1 -p1 -b .coverity
chmod a-x *

%build
#@@@ workaround for #474755 - remove with next update
make clean
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT SBIN_DIR=$RPM_BUILD_ROOT%{_sbindir} MANDIR=$RPM_BUILD_ROOT%{_mandir}

%files
%doc README
%{_sbindir}/sgpio
%{_mandir}/man1/sgpio.*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Jan Synáček <jsynacek@redhat.com> - 1.2.0.10-10
- Use strncpy instead of strcpy (coverity)
- Comment makefile patch

* Mon Nov 19 2012 Jan Synáček <jsynacek@redhat.com> - 1.2.0.10-9
- dos2unix'ed the patch
- Call dos2unix before patching and dos2unix Makefile as well
- Use %%{_sbindir} instead of '/sbin'

* Thu Aug 23 2012 Jan Synáček <jsynacek@redhat.com> - 1.2.0.10-8
- Improve spec

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 05 2012 Jan Synáček <jsynacek@redhat.com> 1.2.0.10-6
- Rebuilt for GCC 4.7

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun  1 2009  Jiri Moskovcak <jmoskovc@redhat.com> 1.2.0.10-3
- rebuild for F12

* Tue Apr 14 2009  Jiri Moskovcak <jmoskovc@redhat.com> 1.2.0.10-2
- move the EOL conversion and the removal of 
  executable bits from %%install to %%prep section

* Wed Dec 10 2008 Jiri Moskovcak <jmoskovc@redhat.com> 1.2.0_10-1
- initial Fedora release
