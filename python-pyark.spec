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
=====
Pyark
=====

|Travis| |PyPi| |License|

.. |Travis| image:: https://img.shields.io/travis/adfinis-sygroup/pyark.svg?style=flat-square
   :target: https://travis-ci.org/adfinis-sygroup/pyark
.. |PyPi| image:: https://img.shields.io/pypi/v/pyark.svg?style=flat-square
   :target: https://pypi.python.org/pypi/pyark
.. |License| image:: https://img.shields.io/github/license/adfinis-sygroup/pyark.svg?style=flat-square
   :target: LICENSE

Pyark is a small python-based CLI tool, which allows you to interact with the
CyberArk Enterprise Password Vault API.

Features
========
Currently the following functionalities are supported:

* Get accounts
* Create accounts
* Delete accounts

Supported authentication methods:

* CyberArk accounts (default)
* RADIUS

Requirements
============
Make sure to have the following Python 3 dependencies installed before using the
tool:

* python-requests

Furthermore it's important to know which version of the CyberArk Password Vault
is used as only the newest versions expose all API endpoints. Make sure to
double check the API documentation, specific for your version, in case the tool
fails to interact with the API.

Installation
============
Simply clone this repository and start using the script. You can also install
it using setup.py or pip.

Examples
========
Get a list of available accounts:

.. code:: shell

   $ pyark --base https://vault.example.com \
           --apiuser foobar                 \
           --apipassword supersecret42      \
           account get                      \
           --safe MySafe                    \
           --keywords bruce

Create a new account:
 
.. code:: shell

   $ pyark --base https://vault.example.com \
           --apiuser foobar                 \
           --apipassword supersecret42      \
           account create                   \
           --safe MySafe                    \
           --platformid TestPlatform        \
           --accountname brucewayne         \
           --address batcave.example.com    \
           --username brucew                \
           --password d4rkkn1ght

Delete an existing account:
 
.. code:: shell

   $ pyark --base https://vault.example.com \
           --apiuser foobar                 \
           --apipassword supersecret42      \
           account delete                   \
           --safe MySafe                    \
           --accountname brucewayne         \
           --keywords bruce

Contributions
=============
Contributions are more than welcome! Please feel free to open new issues or
pull requests.

License 
=======
GNU GENERAL PUBLIC LICENSE Version 3

See the `LICENSE`_ file.

.. _LICENSE: LICENSE


%if 0%{?with_python2}
%description -n python2-pyark
=====
Pyark
=====

|Travis| |PyPi| |License|

.. |Travis| image:: https://img.shields.io/travis/adfinis-sygroup/pyark.svg?style=flat-square
   :target: https://travis-ci.org/adfinis-sygroup/pyark
.. |PyPi| image:: https://img.shields.io/pypi/v/pyark.svg?style=flat-square
   :target: https://pypi.python.org/pypi/pyark
.. |License| image:: https://img.shields.io/github/license/adfinis-sygroup/pyark.svg?style=flat-square
   :target: LICENSE

Pyark is a small python-based CLI tool, which allows you to interact with the
CyberArk Enterprise Password Vault API.

Features
========
Currently the following functionalities are supported:

* Get accounts
* Create accounts
* Delete accounts

Supported authentication methods:

* CyberArk accounts (default)
* RADIUS

Requirements
============
Make sure to have the following Python 3 dependencies installed before using the
tool:

* python-requests

Furthermore it's important to know which version of the CyberArk Password Vault
is used as only the newest versions expose all API endpoints. Make sure to
double check the API documentation, specific for your version, in case the tool
fails to interact with the API.

Installation
============
Simply clone this repository and start using the script. You can also install
it using setup.py or pip.

Examples
========
Get a list of available accounts:

.. code:: shell

   $ pyark --base https://vault.example.com \
           --apiuser foobar                 \
           --apipassword supersecret42      \
           account get                      \
           --safe MySafe                    \
           --keywords bruce

Create a new account:
 
.. code:: shell

   $ pyark --base https://vault.example.com \
           --apiuser foobar                 \
           --apipassword supersecret42      \
           account create                   \
           --safe MySafe                    \
           --platformid TestPlatform        \
           --accountname brucewayne         \
           --address batcave.example.com    \
           --username brucew                \
           --password d4rkkn1ght

Delete an existing account:
 
.. code:: shell

   $ pyark --base https://vault.example.com \
           --apiuser foobar                 \
           --apipassword supersecret42      \
           account delete                   \
           --safe MySafe                    \
           --accountname brucewayne         \
           --keywords bruce

Contributions
=============
Contributions are more than welcome! Please feel free to open new issues or
pull requests.

License 
=======
GNU GENERAL PUBLIC LICENSE Version 3

See the `LICENSE`_ file.

.. _LICENSE: LICENSE

%endif # with_python2

%if 0%{?with_python3}
%description -n python3-pyark
=====
Pyark
=====

|Travis| |PyPi| |License|

.. |Travis| image:: https://img.shields.io/travis/adfinis-sygroup/pyark.svg?style=flat-square
   :target: https://travis-ci.org/adfinis-sygroup/pyark
.. |PyPi| image:: https://img.shields.io/pypi/v/pyark.svg?style=flat-square
   :target: https://pypi.python.org/pypi/pyark
.. |License| image:: https://img.shields.io/github/license/adfinis-sygroup/pyark.svg?style=flat-square
   :target: LICENSE

Pyark is a small python-based CLI tool, which allows you to interact with the
CyberArk Enterprise Password Vault API.

Features
========
Currently the following functionalities are supported:

* Get accounts
* Create accounts
* Delete accounts

Supported authentication methods:

* CyberArk accounts (default)
* RADIUS

Requirements
============
Make sure to have the following Python 3 dependencies installed before using the
tool:

* python-requests

Furthermore it's important to know which version of the CyberArk Password Vault
is used as only the newest versions expose all API endpoints. Make sure to
double check the API documentation, specific for your version, in case the tool
fails to interact with the API.

Installation
============
Simply clone this repository and start using the script. You can also install
it using setup.py or pip.

Examples
========
Get a list of available accounts:

.. code:: shell

   $ pyark --base https://vault.example.com \
           --apiuser foobar                 \
           --apipassword supersecret42      \
           account get                      \
           --safe MySafe                    \
           --keywords bruce

Create a new account:
 
.. code:: shell

   $ pyark --base https://vault.example.com \
           --apiuser foobar                 \
           --apipassword supersecret42      \
           account create                   \
           --safe MySafe                    \
           --platformid TestPlatform        \
           --accountname brucewayne         \
           --address batcave.example.com    \
           --username brucew                \
           --password d4rkkn1ght

Delete an existing account:
 
.. code:: shell

   $ pyark --base https://vault.example.com \
           --apiuser foobar                 \
           --apipassword supersecret42      \
           account delete                   \
           --safe MySafe                    \
           --accountname brucewayne         \
           --keywords bruce

Contributions
=============
Contributions are more than welcome! Please feel free to open new issues or
pull requests.

License 
=======
GNU GENERAL PUBLIC LICENSE Version 3

See the `LICENSE`_ file.

.. _LICENSE: LICENSE

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
%endif # with_python2
%if 0%{?with_python3}
%py3_install
%endif # with_python3

%clean
rm -rf %{buildroot}

%if 0%{with_python2}
%files -n python2-pyark
%defattr(-,root,root,-)
%{python2_sitelib}/*
%endif # with_python2

%if 0%{with_python3}
%files -n python3-pyark
%defattr(-,root,root,-)
%{python3_sitelib}/*
%endif # with_python3

%changelog