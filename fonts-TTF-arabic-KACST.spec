Summary:	Free fonts from King Abdul Aziz City for Science and Technology
Summary(pl.UTF-8):	Wolnodostępne czcionki z King Abdul Aziz City for Science and Technology
Name:		fonts-TTF-arabic-KACST
Version:	2.0
Release:	0.2
License:	GPL
Group:		Fonts
Source0:	http://prdownloads.sourceforge.net/arabeyes/kacst_fonts_%{version}.tar.bz2
# Source0-md5:	d41d8cd98f00b204e9800998ecf8427e
URL:		http://www.arabeyes.org
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
The Khohot project aims at increasing the number of available Arabic free and open
source fonts. The fonts included here come from King Abdul Aziz City for Science
and Technology.

%description -l pl.UTF-8
Celem projektu Khohot jest poszerzenie liczby wolnodostępnych i otwartych czcionek
arabskich. Czcionki zawarte w tej paczce pochodzą z King Abdul Aziz City for Science
and Technology.

%prep
%setup -q -n KacstArabicFonts-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc LICENSE README
%{ttffontsdir}/[Kk]acst*.ttf
