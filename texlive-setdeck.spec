# revision 27997
# category Package
# catalog-ctan /graphics/pgf/contrib/setdeck
# catalog-date 2012-10-17 15:07:15 +0200
# catalog-license gpl3
# catalog-version 0.1
Name:		texlive-setdeck
Version:	0.1
Release:	8
Summary:	Typeset cards for Set
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/setdeck
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/setdeck.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/setdeck.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
