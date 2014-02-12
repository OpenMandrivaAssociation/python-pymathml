%define oname   pymathml
%define debug_package %{nil}

Summary:	Python MathML renderer
Name:		python-pymathml
Version:	0.3
Release:	8
License:	GPL
Group:		Sciences/Mathematics
URL:		http://pymathml.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{oname}/%{oname}-%{version}.tar.bz2
BuildRequires:	python-devel
Requires:	python-libxml2
# rendering backends
Requires:	libnxplot-python
Requires:	pygtk2.0
%rename         pymathml

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
python ./setup.py install --root %{buildroot}

%clean

%files
%doc AUTHORS NEWS PKG-INFO README
%{py_puresitedir}/*
