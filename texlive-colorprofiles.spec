%global tl_name colorprofiles
%global tl_revision 49086

Name:		texlive-%{tl_name}
Epoch:		1
Version:	20181105
Release:	%{tl_revision}.1
Summary:	Collection of free ICC profiles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/colorprofiles
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorprofiles.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorprofiles.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package collects free ICC profiles that can be used by color
profile aware applications/tools like the pdfx package, as well as TeX
and LaTeX packages to access them.

