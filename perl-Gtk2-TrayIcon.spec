%define upstream_name    Gtk2-TrayIcon
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	7

Summary:    Perl module interface to the EggTrayIcon library
License:    GPL+ or Artistic
Group:      Development/GNOME and GTK+
Url:        http://gtk2-perl.sf.net/
Source0:    %{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: glitz-devel
BuildRequires: gtk+2-devel
BuildRequires: perl-Cairo
BuildRequires: perl-ExtUtils-Depends
BuildRequires: perl-ExtUtils-PkgConfig
BuildRequires: perl-Glib >= 0.92
BuildRequires: perl-Gtk2
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: gtk+2
Requires: perl-Gtk2 >= 0.95-6mdk

%description
This module allows a Perl developer to embed an arbitrary widget
in a System Tray like the Gnome notification area.
System Trays are found in both KDE and Gnome.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

#%check
#%make test || :

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc examples/*
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2
%{perl_vendorarch}/auto/*


%changelog
* Wed Jan 25 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.60.0-7
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-4
+ Revision: 702780
- rebuilt against libpng-1.5.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-3
+ Revision: 667190
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 564517
- rebuild for perl 5.12.1

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 408464
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.06-3mdv2009.0
+ Revision: 223783
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.06-2mdv2008.1
+ Revision: 152116
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2008.0
+ Revision: 48051
- new version
  drop translucy patch, merged upstream

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 0.04-8mdv2008.0
+ Revision: 44607
- rebuild

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 0.04-7mdv2008.0
+ Revision: 44600
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.04-6mdv2008.0
+ Revision: 23405
- rebuild


* Wed Mar 01 2006 Frederic Crozat <fcrozat@mandriva.com> 0.04-5mdk
- Patch0 (danw): Fix tray icon transparency in KDE notification area

* Fri Dec 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-4mdk
- Fix Buildrequires

* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-3mdk
- Fix BuildRequires

* Mon Nov 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.04-2mdk
- rebuild for new perl

* Mon Apr 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-1mdk
- new release

* Thu Feb 26 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.03-3mdk
- rebuild
- own dir

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.03-2mdk
- add example

* Mon Nov 24 2003 Daouda LO <daouda@mandrakesoft.com> 0.03-1mdk
- First Mandrake Package

