Summary: Modify rpath of compiled programs
Name: chrpath
Version: 0.13
Release: 7%{?dist}
License: GPL+
Group: Development/Tools
URL: http://ftp.tux.org/pub/X-Windows/ftp.hungry.com/chrpath/
Patch0: chrpath-0.13-NULL-entry.patch
Source0: http://ftp.tux.org/pub/X-Windows/ftp.hungry.com/chrpath/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%prep
%setup -q
%patch0 -p1 -b .NULL

%build
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -fr %{buildroot}/usr/doc

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README NEWS ChangeLog*
%{_bindir}/chrpath
%{_mandir}/man1/chrpath.1*

%changelog
* Wed Jan 06 2010 Daniel Novotny <dnovotny@redhat.com> 0.13-7
- fix broken upstream URL

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.13-6.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.13-5
- Fix last entry in .dynamic (by Christian Krause <chkr@plauener.de>).

* Sat Sep  8 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.13-2
- License: GPL+

* Sun Mar 12 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.13-1
- Initial build.

