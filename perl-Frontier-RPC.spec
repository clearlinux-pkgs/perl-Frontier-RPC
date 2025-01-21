#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : perl-Frontier-RPC
Version  : 0.07b4
Release  : 35
URL      : https://cpan.metacpan.org/authors/id/K/KM/KMACLEOD/Frontier-RPC-0.07b4.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KM/KMACLEOD/Frontier-RPC-0.07b4.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfrontier-rpc-perl/libfrontier-rpc-perl_0.07b4-7.debian.tar.xz
Summary  : Perl module for RPC over XML
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Frontier-RPC-license = %{version}-%{release}
Requires: perl-Frontier-RPC-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTTP::Daemon)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(LWP::MediaTypes)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)
BuildRequires : perl(XML::Parser)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Frontier::RPC implements UserLand Software's XML RPC (Remote Procedure
Calls using Extensible Markup Language).  Frontier::RPC includes both
a client module for making requests to a server and a daemon module
for implementing servers.  Frontier::RPC uses RPC2 format messages.

%package dev
Summary: dev components for the perl-Frontier-RPC package.
Group: Development
Provides: perl-Frontier-RPC-devel = %{version}-%{release}
Requires: perl-Frontier-RPC = %{version}-%{release}

%description dev
dev components for the perl-Frontier-RPC package.


%package license
Summary: license components for the perl-Frontier-RPC package.
Group: Default

%description license
license components for the perl-Frontier-RPC package.


%package perl
Summary: perl components for the perl-Frontier-RPC package.
Group: Default
Requires: perl-Frontier-RPC = %{version}-%{release}

%description perl
perl components for the perl-Frontier-RPC package.


%prep
%setup -q -n Frontier-RPC-0.07b4
cd %{_builddir}
tar xf %{_sourcedir}/libfrontier-rpc-perl_0.07b4-7.debian.tar.xz
cd %{_builddir}/Frontier-RPC-0.07b4
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Frontier-RPC-0.07b4/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Frontier-RPC
cp %{_builddir}/Frontier-RPC-%{version}/COPYING %{buildroot}/usr/share/package-licenses/perl-Frontier-RPC/f5a13608797f9dce482939e43d7594beec511188 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Frontier-RPC/5d26a4cb2c5570c5c164b7736663276a02ae3b61 || :
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Apache::XMLRPC.3
/usr/share/man/man3/Frontier::Client.3
/usr/share/man/man3/Frontier::Daemon.3
/usr/share/man/man3/Frontier::RPC2.3
/usr/share/man/man3/Frontier::Responder.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Frontier-RPC/5d26a4cb2c5570c5c164b7736663276a02ae3b61
/usr/share/package-licenses/perl-Frontier-RPC/f5a13608797f9dce482939e43d7594beec511188

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
