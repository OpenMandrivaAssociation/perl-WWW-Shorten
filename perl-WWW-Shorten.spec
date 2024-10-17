%define upstream_name    WWW-Shorten
%define upstream_version 3.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl interface to makeashorterlink.com

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Config::Auto)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(LWP) >= 5.750.0
BuildRequires:	perl(LWP::UserAgent) >= 2.23.0
BuildRequires:	perl(Module::Build) >= 0.380.0
BuildRequires:	perl(Test::More) >= 0.470.0
BuildRequires:	perl(URI) >= 1.270.0
BuildArch:	noarch

%description
The function 'makeashorterlink' will call the relevant web site passing it
your long URL and will return the shorter version.

The function 'makealongerlink' does the reverse. 'makealongerlink' will
accept as an argument either the full shortened URL or just the identifier.

If anything goes wrong, then either function will return 'undef'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Don't run tests that depend on network
make test TEST_FILES="t/0*.t t/9*.t"

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/shorten
%{_mandir}/man1/shorten.1*



