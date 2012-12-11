%define oname   pymathml
%define version 0.3
%define release %mkrel 7

Summary:	Python MathML renderer
Name:		python-pymathml
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sciences/Mathematics
URL:		http://pymathml.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{oname}/%{oname}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel
Requires:	python-libxml2
# rendering backends
Requires:	libnxplot-python
Requires:	pygtk2.0
Provides:	pymathml = %{version}-%{release}
Obsoletes:      pymathml < %{version}

%description
The goal of %{oname} is to create a system-independent MathML
rendering engine in Python. This engine works with an abstract
'plotter' driver class, that can be subclassed for any rendering
device needed.

%prep
%setup -q -n %{oname}-%{version}

%build
python ./setup.py build

%install
rm -rf %{buildroot}
python ./setup.py install --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS PKG-INFO README
%py_puresitedir/*


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3-7mdv2010.0
+ Revision: 442436
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.3-6mdv2009.1
+ Revision: 323949
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3-5mdv2009.0
+ Revision: 242461
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 24 2007 Funda Wang <fwang@mandriva.org> 0.3-3mdv2008.0
+ Revision: 54912
- Provides old lib


* Tue Jan 30 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.3-2mdv2007.0
+ Revision: 115362
- Rebuild for new python
- Rebuild according to the policy
- Import pymathml

