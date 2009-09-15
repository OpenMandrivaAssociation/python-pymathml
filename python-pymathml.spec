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
