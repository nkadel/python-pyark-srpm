#
# spec file for package python-pyark
#
# Copyright (c) 2018 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL does not include python3 by default
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%else
%global with_python3 0
%endif

# Fedora > 28 no longer publishes python2 by default
%if 0%{?fedora} > 28
%global with_python2 0
%else
%global with_python2 1
%endif

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Common SRPM package
Name:           python-pyark
Version:        1.1.1
Release:        0.1
Url:            https://github.com/adfinis-sygroup/pyark
Summary:        Pyark is a small python-based CLI tool, which allows you to interact with the CyberArk Enterprise Password Vault API.
License:        GNU General Public License v3 (GPLv3) (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pyark/pyark-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?with_python2}
BuildRequires:  python2-devel
%endif # with_python2
%if 0%{?with_python3}
BuildRequires:  python3-devel
%endif # with_python3

%if 0%{?with_python2}
%package -n python2-pyark
Version:        1.1.1
Release:        0
Url:            https://github.com/adfinis-sygroup/pyark
Summary:        Pyark is a small python-based CLI tool, which allows you to interact with the CyberArk Enterprise Password Vault API.
License:        GNU General Public License v3 (GPLv3) (FIXME:No SPDX)
%if 0%{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python2-%{srcname}}
%endif # with_python2

%if 0%{?with_python3}
%package -n python3-pyark
Version:        1.1.1
Release:        0
Url:            https://github.com/adfinis-sygroup/pyark
Summary:        Pyark is a small python-based CLI tool, which allows you to interact with the CyberArk Enterprise Password Vault API.
License:        GNU General Public License v3 (GPLv3) (FIXME:No SPDX)
%if 0%{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python2-%{srcname}}
%endif # with_python3

%description
Pyark is a small python-based CLI tool, which allows you to interact with the
CyberArk Enterprise Password Vault API.

%if 0%{?with_python2}
%description -n python2-pyark
Pyark is a small python-based CLI tool, which allows you to interact with the
CyberArk Enterprise Password Vault API.
%endif # with_python2

%if 0%{?with_python3}
%description -n python3-pyark
Pyark is a small python-based CLI tool, which allows you to interact with the
CyberArk Enterprise Password Vault API.
%endif # with_python3

%prep
%setup -q -n pyark-%{version}

%build
%if 0%{?with_python2}
%py2_build
%endif # with_python2
%if 0%{?with_python3}
%py2_build
%endif # with_python3

%install
%if 0%{?with_python2}
%py2_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/pyark $RPM_BUILD_ROOT%{_bindir}/pyark2
%{__ln_s} pyark2 $RPM_BUILD_ROOT%{_bindir}/pyark
%endif # with_python2
%if 0%{?with_python3}
%py3_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/pyark $RPM_BUILD_ROOT%{_bindir}/pyark3
%{__ln_s} pyark3 $RPM_BUILD_ROOT%{_bindir}/pyark
%endif # with_python3

%clean
rm -rf %{buildroot}

%if 0%{with_python2}
%files -n python2-pyark
%defattr(-,root,root,-)
%{python2_sitelib}/*
%{_bindir}/pyark2
%if ! 0%{with_python3}
%{_bindir}/pyark
%endif
%endif # with_python2

%if 0%{with_python3}
%files -n python3-pyark
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/pyark3
%{_bindir}/pyark
%endif # with_python3

%changelog
