### RPM external lcov 1.9
## NOCOMPILER
Source: http://heanet.dl.sourceforge.net/sourceforge/ltp/%n-%realversion.tar.gz
Patch0: lcov-merge-files-in-same-dir

%prep
%setup -n %n-%realversion
%patch0 -p1

%ifos darwin
# OS X does not support -D option
sed -ibak 's/install -p -D/install -p/g' bin/install.sh
%endif

%build
make %makeprocesses

%install
mkdir -p %i/bin
make PREFIX=%i BIN_DIR=%i/bin install
