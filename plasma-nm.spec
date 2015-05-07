%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Plasma applet written in QML for managing network connections
Name:		plasma-nm5
Version:	5.3.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/network/plasma-nm
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{major}/plasma-nm-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5ModemManagerQt)
BuildRequires:	cmake(KF5NetworkManagerQt)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	pkgconfig(NetworkManager) >= 0.9.8
BuildRequires:	pkgconfig(openconnect) >= 3.99
BuildRequires:	pkgconfig(mobile-broadband-provider-info)
BuildRequires:	pkgconfig(ModemManager)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(libnm)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-util)
Requires:	mobile-broadband-provider-info
Requires:	modemmanager
Requires:	networkmanager
Conflicts:	plasma-applet-networkmanagement
Conflicts:	knetworkmanager-common
Conflicts:	plasma-nm < 0.9.3.7
Obsoletes:	plasma-applet-networkmanagement <= 0.9.0.9-2

%description
Plasma applet and editor for managing your network connections in KDE5 using
the default NetworkManager service.

%files -f %{name}.lang
%{_bindir}/kde5-nm-connection-editor
%{_libdir}/libplasmanm_*.so
%{_libdir}/qt5/plugins/kded_networkmanagement.so
%{_libdir}/qt5/plugins/libplasmanetworkmanagement_*.so
%{_libdir}/qt5/qml/org/kde/plasma/networkmanagement
%{_datadir}/applications/kde5-nm-connection-editor.desktop
%{_datadir}/kxmlgui5/kde5-nm-connection-editor
%{_datadir}/knotifications5/networkmanagement.notifyrc
%{_datadir}/kservices5/kded/networkmanagement.desktop
%{_datadir}/kservices5/plasmanetworkmanagement*.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.networkmanagement.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.networkmanagement
%{_datadir}/kservicetypes5/plasma-networkmanagement*.desktop

#----------------------------------------------------------------------------

%prep
%setup -qn plasma-nm-%{version}
%apply_patches
# Workaround for clang bug causing a compiler crash
#export CXX=g++
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang \
	kde5-nm-connection-editor \
	plasma_applet_org.kde.plasma.networkmanagement \
	plasmanetworkmanagement-libs \
	plasmanetworkmanagement-kded \
	plasmanetworkmanagement_l2tpui \
	plasmanetworkmanagement_openconnectui \
	plasmanetworkmanagement_openswanui \
	plasmanetworkmanagement_openvpnui \
	plasmanetworkmanagement_pptpui \
	plasmanetworkmanagement_strongswanui \
	plasmanetworkmanagement_vpncui \
	%{name}.lang

