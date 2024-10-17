Name:		texlive-setdeck
Version:	40613
Release:	2
Summary:	Typeset cards for Set
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/setdeck
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/setdeck.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/setdeck.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package will typeset cards for use in a game of Set.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/setdeck/setdeck.sty
%doc %{_texmfdistdir}/doc/latex/setdeck/README
%doc %{_texmfdistdir}/doc/latex/setdeck/setdeck.pdf
%doc %{_texmfdistdir}/doc/latex/setdeck/setdeck.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
