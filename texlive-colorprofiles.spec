Name:		texlive-colorprofiles
Version:	49086
Release:	2
Summary:	Collection of free ICC profiles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/colorprofiles
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorprofiles.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorprofiles.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package collects free ICC profiles that can be used by
color profile aware applications/tools like the pdfx package,
as well as TeX and LaTeX packages to access them.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/colorprofiles
%doc %{_texmfdistdir}/doc/generic/colorprofiles

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
