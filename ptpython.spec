Name:           ptpython
Version:        3.0.19
Release:        1
Summary:        Python REPL build on top of prompt_toolkit

License:        BSD
URL:            https://github.com/prompt-toolkit/ptpython
Source0:        %name-%version.tar.gz
Requires:       python3-appdirs
Requires:       python3-importlib_metadata
Requires:       python3-jedi
Requires:       python3-prompt_toolkit
Requires:       python3-pygments

BuildArch:      noarch

%description
Ptpython is an advanced Python REPL built on top of the prompt_toolkit library.
It features syntax highlighting, multiline editing (the up arrow works),
autocompletion, mouse support, support for color schemes, support for bracketed
paste, both Vi and Emacs key bindings, support for double width (Chinese)
characters, and many other things.}


%prep
%setup -q

%build
%{py3_build}

%install
%{py3_install}

%files
%license LICENSE
%doc CHANGELOG README.rst
%{python3_sitelib}/ptpython
%{python3_sitelib}/ptpython-%{version}-py%{python3_version}.egg-info
%{_bindir}/ptpython
%{_bindir}/ptpython3
%{_bindir}/ptpython%{python3_version}
%{_bindir}/ptipython
%{_bindir}/ptipython3
%{_bindir}/ptipython%{python3_version}


%changelog
* Fri Jul 16 2021  Chao Li <clouds@isrc.iscas.ac.cn> - 3.0.19-1
- First packaging of version 3.0.19

