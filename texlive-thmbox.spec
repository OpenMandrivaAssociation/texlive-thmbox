# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/thmbox
# catalog-date 2009-03-25 08:55:29 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-thmbox
Version:	20090325
Release:	8
Summary:	Decorate theorem statements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thmbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thmbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thmbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thmbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines an environment thmbox that presents
theorems, definitions and similar objects in boxes decorated
with frames and various aesthetic features. The standard macro
\newtheorem may be redefined to use the environment.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/thmbox/thmbox.sty
%doc %{_texmfdistdir}/doc/latex/thmbox/README
%doc %{_texmfdistdir}/doc/latex/thmbox/thmbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/thmbox/thmbox.dtx
%doc %{_texmfdistdir}/source/latex/thmbox/thmbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090325-2
+ Revision: 756833
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090325-1
+ Revision: 719729
- texlive-thmbox
- texlive-thmbox
- texlive-thmbox

