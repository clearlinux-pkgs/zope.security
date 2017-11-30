#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF2A968348913D1D8 (tseaver@palladion.com)
#
Name     : zope.security
Version  : 4.1.1
Release  : 5
URL      : https://pypi.debian.net/zope.security/zope.security-4.1.1.tar.gz
Source0  : https://pypi.debian.net/zope.security/zope.security-4.1.1.tar.gz
Source99 : https://pypi.debian.net/zope.security/zope.security-4.1.1.tar.gz.asc
Summary  : Zope Security Framework
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.security-legacypython
Requires: zope.security-python3
Requires: zope.security-python
Requires: Sphinx
Requires: coverage
Requires: nose
Requires: pytz
Requires: setuptools
Requires: zope.i18nmessageid
Requires: zope.interface
Requires: zope.location
Requires: zope.proxy
Requires: zope.schema
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : zope.i18nmessageid
BuildRequires : zope.interface
BuildRequires : zope.location
BuildRequires : zope.proxy
BuildRequires : zope.schema

%description
=================

%package legacypython
Summary: legacypython components for the zope.security package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the zope.security package.


%package python
Summary: python components for the zope.security package.
Group: Default
Requires: zope.security-legacypython
Requires: zope.security-python3

%description python
python components for the zope.security package.


%package python3
Summary: python3 components for the zope.security package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.security package.


%prep
%setup -q -n zope.security-4.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512085682
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :
%install
export SOURCE_DATE_EPOCH=1512085682
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
