#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.security
Version  : 4.2.2
Release  : 13
URL      : https://pypi.debian.net/zope.security/zope.security-4.2.2.tar.gz
Source0  : https://pypi.debian.net/zope.security/zope.security-4.2.2.tar.gz
Summary  : Zope Security Framework
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.security-python3
Requires: zope.security-license
Requires: zope.security-python
Requires: Sphinx
Requires: pytz
Requires: setuptools
Requires: zope.component
Requires: zope.configuration
Requires: zope.i18nmessageid
Requires: zope.interface
Requires: zope.location
Requires: zope.proxy
Requires: zope.schema
Requires: zope.testing
Requires: zope.testrunner
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : zope.i18nmessageid
BuildRequires : zope.interface
BuildRequires : zope.location
BuildRequires : zope.proxy
BuildRequires : zope.schema

%description
zope.security
        ===============

%package license
Summary: license components for the zope.security package.
Group: Default

%description license
license components for the zope.security package.


%package python
Summary: python components for the zope.security package.
Group: Default
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
%setup -q -n zope.security-4.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529091390
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/zope.security
cp LICENSE.txt %{buildroot}/usr/share/doc/zope.security/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/zope.security/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
