#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Cookie
%define		pnam	Baker
%include	/usr/lib/rpm/macros.perl
Summary:	Cookie::Baker - Cookie string generator / parser
Name:		perl-Cookie-Baker
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Cookie/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bc8f95893d6ec3093a62d1957e1908f2
URL:		http://search.cpan.org/dist/Cookie-Baker/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-URI
BuildRequires:	perl(Test::Time)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cookie::Baker provides simple cookie string generator and parser.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--destdir=$RPM_BUILD_ROOT \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Cookie
%{perl_vendorlib}/Cookie/*.pm
%{_mandir}/man3/*
