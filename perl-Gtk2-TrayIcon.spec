%define upstream_name    Gtk2-TrayIcon
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 6

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
