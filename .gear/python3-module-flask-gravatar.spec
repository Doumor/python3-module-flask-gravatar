%define pypi_name flask-gravatar

%def_without check

Name:    python3-module-%pypi_name
Version: 0.5.0
Release: alt1

Summary: Small and simple gravatar usage in Flask
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/Flask-Gravatar/
VCS:     https://github.com/zzzsochi/Flask-Gravatar

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-flask
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-Pygments
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup
# Get rid of stale dependencies
sed -i 's/--pep8 //' pytest.ini
sed -i '/pytest-runner/d' setup.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst CHANGES.rst RELEASE-NOTES.rst AUTHORS LICENSE
%python3_sitelibdir/flask_gravatar
%python3_sitelibdir/Flask_Gravatar-%version.dist-info

%changelog
* Wed Oct 4 2023 Danilkin Danila <danild@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
