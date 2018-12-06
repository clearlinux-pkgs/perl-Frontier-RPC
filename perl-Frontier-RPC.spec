#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Frontier-RPC
Version  : 0.07b4
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/K/KM/KMACLEOD/Frontier-RPC-0.07b4.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KM/KMACLEOD/Frontier-RPC-0.07b4.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfrontier-rpc-perl/libfrontier-rpc-perl_0.07b4-7.debian.tar.xz
Summary  : Perl module for RPC over XML
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Frontier-RPC-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTTP::Daemon)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(LWP::MediaTypes)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)
BuildRequires : perl(XML::Parser)

%description
Frontier::RPC implements UserLand Software's XML RPC (Remote Procedure
Calls using Extensible Markup Language).  Frontier::RPC includes both
a client module for making requests to a server and a daemon module
for implementing servers.  Frontier::RPC uses RPC2 format messages.

%package dev
Summary: dev components for the perl-Frontier-RPC package.
Group: Development
Provides: perl-Frontier-RPC-devel = %{version}-%{release}

%description dev
dev components for the perl-Frontier-RPC package.


%package license
Summary: license components for the perl-Frontier-RPC package.
Group: Default

%description license
license components for the perl-Frontier-RPC package.


%prep
%setup -q -n Frontier-RPC-0.07b4
cd ..
%setup -q -T -D -n Frontier-RPC-0.07b4 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Frontier-RPC-0.07b4/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Frontier-RPC
cp COPYING %{buildroot}/usr/share/package-licenses/perl-Frontier-RPC/COPYING
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Frontier-RPC/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Apache/XMLRPC.pm
/usr/lib/perl5/vendor_perl/5.28.1/Frontier/Client.pm
/usr/lib/perl5/vendor_perl/5.28.1/Frontier/Daemon.pm
/usr/lib/perl5/vendor_perl/5.28.1/Frontier/RPC2.pm
/usr/lib/perl5/vendor_perl/5.28.1/Frontier/Responder.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Apache::XMLRPC.3
/usr/share/man/man3/Frontier::Client.3
/usr/share/man/man3/Frontier::Daemon.3
/usr/share/man/man3/Frontier::RPC2.3
/usr/share/man/man3/Frontier::Responder.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Frontier-RPC/COPYING
/usr/share/package-licenses/perl-Frontier-RPC/deblicense_copyright
