#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD3657D24D058434C (petri@digip.org)
#
Name     : jansson
Version  : 2.12
Release  : 3
URL      : http://www.digip.org/jansson/releases/jansson-2.12.tar.gz
Source0  : http://www.digip.org/jansson/releases/jansson-2.12.tar.gz
Source99 : http://www.digip.org/jansson/releases/jansson-2.12.tar.gz.asc
Summary  : Library for encoding, decoding and manipulating JSON data
Group    : Development/Tools
License  : MIT
Requires: jansson-lib = %{version}-%{release}
Requires: jansson-license = %{version}-%{release}

%description
To build the documentation, invoke
make html
Then point your browser to _build/html/index.html.

%package dev
Summary: dev components for the jansson package.
Group: Development
Requires: jansson-lib = %{version}-%{release}
Provides: jansson-devel = %{version}-%{release}

%description dev
dev components for the jansson package.


%package lib
Summary: lib components for the jansson package.
Group: Libraries
Requires: jansson-license = %{version}-%{release}

%description lib
lib components for the jansson package.


%package license
Summary: license components for the jansson package.
Group: Default

%description license
license components for the jansson package.


%prep
%setup -q -n jansson-2.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544716099
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1544716099
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jansson
cp LICENSE %{buildroot}/usr/share/package-licenses/jansson/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libjansson.so
/usr/lib64/pkgconfig/jansson.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libjansson.so.4
/usr/lib64/libjansson.so.4.11.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jansson/LICENSE
