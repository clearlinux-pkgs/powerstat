#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : powerstat
Version  : 0.02.26
Release  : 2
URL      : https://kernel.ubuntu.com/~cking/tarballs/powerstat/powerstat-0.02.26.tar.gz
Source0  : https://kernel.ubuntu.com/~cking/tarballs/powerstat/powerstat-0.02.26.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: powerstat-bin = %{version}-%{release}
Requires: powerstat-data = %{version}-%{release}
Requires: powerstat-license = %{version}-%{release}
Requires: powerstat-man = %{version}-%{release}

%description
No detailed description available

%package bin
Summary: bin components for the powerstat package.
Group: Binaries
Requires: powerstat-data = %{version}-%{release}
Requires: powerstat-license = %{version}-%{release}

%description bin
bin components for the powerstat package.


%package data
Summary: data components for the powerstat package.
Group: Data

%description data
data components for the powerstat package.


%package license
Summary: license components for the powerstat package.
Group: Default

%description license
license components for the powerstat package.


%package man
Summary: man components for the powerstat package.
Group: Default

%description man
man components for the powerstat package.


%prep
%setup -q -n powerstat-0.02.26
cd %{_builddir}/powerstat-0.02.26

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625034232
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1625034232
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/powerstat
cp %{_builddir}/powerstat-0.02.26/COPYING %{buildroot}/usr/share/package-licenses/powerstat/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/powerstat

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/powerstat

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/powerstat/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/powerstat.8.gz
