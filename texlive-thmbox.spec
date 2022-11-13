Name:		texlive-thmbox
Version:	15878
Release:	1
Summary:	Decorate theorem statements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thmbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thmbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thmbox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thmbox.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
