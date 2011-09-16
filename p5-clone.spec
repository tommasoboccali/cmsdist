### RPM external p5-clone 0.31
## INITENV +PATH PERL5LIB %i/lib/perl5
%define downloadn Clone
Source: http://search.cpan.org/CPAN/authors/id/R/RD/RDF/%{downloadn}-%{realversion}.tar.gz
Requires: p5-extutils-makemaker

%prep
%setup -n %downloadn-%realversion

%build
LC_ALL=C; export LC_ALL
perl Makefile.PL INSTALL_BASE=%i
make

%install
make install
rm -rf %i/man
