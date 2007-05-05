%define module TrayIcon

Summary: Perl module interface to the EggTrayIcon library
Name:    perl-Gtk2-%module
Version: 0.04
Release: %mkrel 6
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  Gtk2-%module-%version.tar.bz2
# (fc) 0.04-3mdk fix transparency in KDE notification area
Patch0: Gtk2-TrayIcon-0.04-transparency.patch
URL: http://gtk2-perl.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk+2-devel perl-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Glib >= 0.92
BuildRequires: perl-Gtk2
BuildRequires: glitz-devel
BuildRequires: perl-Cairo
Requires: gtk+2 perl-Gtk2 >= 0.95-6mdk

%description
This module allows a Perl developer to embed an arbitrary widget
in a System Tray like the Gnome notification area.
System Trays are found in both KDE and Gnome.

%prep
%setup -q -n Gtk2-%module-%version
%patch0 -p1 -b .transparency
find -type d -name CVS | rm -rf 
perl Makefile.PL INSTALLDIRS=vendor

%build
%make OPTIMIZE="$RPM_OPT_FLAGS"

#%check
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc examples/*
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2
%{perl_vendorarch}/auto/*

