Summary:	A commandline metalink generator
Name:		metalink
Version:	0.3.6
Release:	%mkrel 2
Group:		Networking/Other
License:	GPLv3+
URL:		http://metamirrors.nl/metalinks_project
Source0:	http://downloads.sourceforge.net/metalinks/%{name}-%{version}.tar.gz
BuildRequires:	boost-devel
BuildRequires:	glibmm2.4-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	libicu-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A .metalink is an XML file that describes a download, and includes mirrors
and checksum information. Metalink is the main Metalink generation tool.
It combines a list of mirrors (from stdin) and a number of files into one
Metalink record (stdout). It can also be used to transform a MD5SUMS file
into a metalink.


%prep

%setup -q
chmod 0644 example/gen.sh

%build
rm -rf autom4te.cache

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std INSTALL="install -p"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO example
%{_bindir}/metalink
%{_mandir}/man1/*

