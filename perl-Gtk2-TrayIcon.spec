%define modname	Gtk2-TrayIcon
%define modver	0.06

Summary:	Perl module interface to the EggTrayIcon library
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	20
License:	GPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Url:		https://gtk2-perl.sf.net/
Source0:	%{modname}-%{modver}.tar.bz2
Source100:	%{name}.rpmlintrc
BuildRequires:	perl-Cairo
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-Glib >= 0.92
BuildRequires:	perl-Gtk2
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(glitz)
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	gtk+2
Requires:	perl-Gtk2

%description
This module allows a Perl developer to embed an arbitrary widget
in a System Tray like the Gnome notification area.
System Trays are found in both KDE and Gnome.

%prep
%autosetup -p1 -n %{modname}-%{modver}
find -type d -name CVS | rm -rf 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
#%make test || :

%install
%make_install

%files
%doc examples/*
%{perl_vendorarch}/Gtk2
%{perl_vendorarch}/auto/*
%doc %{_mandir}/man3/*

