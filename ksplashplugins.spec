#
# TODO: Fixing descriptions
#

Summary:	Plugins for new KDE splash
Summary(pl):	Wtyczki do nowego splasha KDE
Name:		ksplashplugins
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.eleceng.ohio-state.edu/~ravi/%{name}-%{version}.tar.gz
# Source0-md5: 9baa36a5f0f88423634c4c6bb11c7669
Patch0:		%{name}-fix-xconfig.h.patch
BuildRequires:	kdebase-devel >= 3.2-0.030410.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for new KDE splash.

%description -l pl
Wtyczki do nowego splasha KDE.

%package -n kde-splashplugin-2k
Summary:	ksplash plugin 2k
Summary(pl):	Wtyczka ksplash 2k
Group:		X11/Amusements
Provides:	ksplashplugin
Requires:	kdebase >= 3.2-0.030410.1

%description -n kde-splashplugin-2k
ksplash plugin 2k.

%description -n kde-splashplugin-2k -l pl
Wtyczka ksplash 2k.

%package -n kde-splashplugin-MacClassic
Summary:	ksplash plugin MacClassic
Summary(pl):	Wtyczka ksplash MacClassic
Group:		X11/Amusements
Provides:	ksplashplugin
Requires:	kdebase >= 3.2-0.030410.1

%description -n kde-splashplugin-MacClassic
ksplash plugin MacClassic.

%description -n kde-splashplugin-MacClassic -l pl
Wtyczka ksplash MacClassic.

%package -n kde-splashplugin-MacX
Summary:	ksplash plugin MacX
Summary(pl):	Wtyczka ksplash MacX
Group:		X11/Amusements
Provides:	ksplashplugin
Requires:	kdebase >= 3.2-0.030410.1

%description -n kde-splashplugin-MacX
ksplash plugin MacX.

%description -n kde-splashplugin-MacX -l pl
Wtyczka ksplash MacX.

%package -n kde-splashplugin-Standard
Summary:	ksplash plugin Standard
Summary(pl):	Wtyczka ksplash Standard
Group:		X11/Amusements
Provides:	ksplashplugin
Requires:	kdebase >= 3.2-0.030410.1

%description -n kde-splashplugin-Standard
ksplash plugin Standard.

%description -n kde-splashplugin-Standard -l pl
Wtyczka ksplash Standard.

%package -n kde-splashplugin-XpLike
Summary:	ksplash plugin XpLike
Summary(pl):	Wtyczka ksplash XpLike
Group:		X11/Amusements
Provides:	ksplashplugin
Requires:	kdebase >= 3.2-0.030410.1

%description -n kde-splashplugin-XpLike
ksplash plugin XpLike.

%description -n kde-splashplugin-XpLike -l pl
Wtyczka ksplash XpLike.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-splashplugin-2k
%defattr(644,root,root,755)
%{_libdir}/kde3/libksplash2k.la
%attr(755,root,root) %{_libdir}/kde3/libksplash2k.so*
%{_datadir}/apps/ksplash/Themes/2k
%{_datadir}/services/ksplash2k.desktop

%files -n kde-splashplugin-MacClassic
%defattr(644,root,root,755)
%{_libdir}/kde3/libksplashmacclassic.la
%attr(755,root,root) %{_libdir}/kde3/libksplashmacclassic.so*
%{_datadir}/apps/ksplash/Themes/MacClassic
%{_datadir}/services/ksplashmacclassic.desktop

%files -n kde-splashplugin-MacX
%defattr(644,root,root,755)
%{_libdir}/kde3/libksplashmacx.la
%attr(755,root,root) %{_libdir}/kde3/libksplashmacx.so*
%{_datadir}/apps/ksplash/Themes/MacX
%{_datadir}/services/ksplashmacx.desktop

%files -n kde-splashplugin-Standard
%defattr(644,root,root,755)
%{_libdir}/kde3/libksplashstandard.la
%attr(755,root,root) %{_libdir}/kde3/libksplashstandard.so*
%{_datadir}/apps/ksplash/Themes/Standard
%{_datadir}/services/ksplashstandard.desktop

%files -n kde-splashplugin-XpLike
%defattr(644,root,root,755)
%{_libdir}/kde3/libksplashxplike.la
%attr(755,root,root) %{_libdir}/kde3/libksplashxplike.so*
%{_datadir}/apps/ksplash/Themes/XpLike
%{_datadir}/services/ksplashxplike.desktop
