#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.security
Version  : 5.1.1
Release  : 43
URL      : https://files.pythonhosted.org/packages/5c/67/73fbf688b3b0a9b33ece0622b06065ee3bea70acebf8e15fa08d9a8f06de/zope.security-5.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/5c/67/73fbf688b3b0a9b33ece0622b06065ee3bea70acebf8e15fa08d9a8f06de/zope.security-5.1.1.tar.gz
Summary  : Zope Security Framework
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.security-license = %{version}-%{release}
Requires: zope.security-python = %{version}-%{release}
Requires: zope.security-python3 = %{version}-%{release}
Requires: setuptools
Requires: zope.component
Requires: zope.i18nmessageid
Requires: zope.interface
Requires: zope.location
Requires: zope.proxy
Requires: zope.schema
BuildRequires : buildreq-distutils3
BuildRequires : setuptools
BuildRequires : zope.component
BuildRequires : zope.i18nmessageid
BuildRequires : zope.interface
BuildRequires : zope.location
BuildRequires : zope.proxy
BuildRequires : zope.schema

%description
===============
zope.security
===============
.. image:: https://img.shields.io/pypi/v/zope.security.svg
:target: https://pypi.python.org/pypi/zope.security/
:alt: Latest release

%package license
Summary: license components for the zope.security package.
Group: Default

%description license
license components for the zope.security package.


%package python
Summary: python components for the zope.security package.
Group: Default
Requires: zope.security-python3 = %{version}-%{release}

%description python
python components for the zope.security package.


%package python3
Summary: python3 components for the zope.security package.
Group: Default
Requires: python3-core
Provides: pypi(zope.security)
Requires: pypi(setuptools)
Requires: pypi(zope.component)
Requires: pypi(zope.i18nmessageid)
Requires: pypi(zope.interface)
Requires: pypi(zope.location)
Requires: pypi(zope.proxy)
Requires: pypi(zope.schema)

%description python3
python3 components for the zope.security package.


%prep
%setup -q -n zope.security-5.1.1
cd %{_builddir}/zope.security-5.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585000772
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.security
cp %{_builddir}/zope.security-5.1.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.security/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.security/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
