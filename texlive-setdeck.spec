%global tl_name setdeck
%global tl_revision 40613

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Typeset cards for Set
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/setdeck
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/setdeck.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/setdeck.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package will typeset cards for use in a game of Set.

