Summary:	A commandline metalink generator
Name:		metalink
Version:	0.3.6
Release:	3
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



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.6-2mdv2011.0
+ Revision: 612851
- the mass rebuild of 2010.1 packages

* Mon Nov 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3.6-1mdv2010.1
+ Revision: 463503
- import metalink


* Mon Nov 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3.6-1mdv2010.0
- initial Mandriva package (fedora import)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jan 05 2009 Ant Bryan <anthonybryan at gmail.com> - 0.3.6-2
- New version, 0.3.6-2
- man page, licensing clarification upstream.

* Mon Dec 08 2008 Ant Bryan <anthonybryan at gmail.com> - 0.3.5-1
- 0.3.5-1
