Summary:	Plasma applet written in QML for managing network connections
Name:		plasma-nm5
Version:	5.0.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/network/plasma-nm
Source0:	ftp://ftp.kde.org/pub/kde/stable/plasma/%{version}/plasma-nm-%{version}.tar.xz
BuildRequires:	mobile-broadband-provider-info
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5ModemManagerQt)
BuildRequires:	cmake(KF5NetworkManagerQt)
BuildRequires:	pkgconfig(NetworkManager) >= 0.9.8
BuildRequires:	pkgconfig(openconnect) >= 3.99
Requires:	mobile-broadband-provider-info
Requires:	modemmanager
Requires:	networkmanager
Conflicts:	plasma-applet-networkmanagement
Conflicts:	knetworkmanager-common
Obsoletes:	plasma-applet-networkmanagement <= 0.9.0.9-2

%description
Plasma applet and editor for managing your network connections in KDE5 using
the default NetworkManager service.

%files -f %{name}.lang
%{_bindir}/kde5-nm-connection-editor
%{_libdir}/libplasmanm_*.so
%{_libdir}/plugins/kded_networkmanagement.so
%{_libdir}/plugins/libplasmanetworkmanagement_*.so
%{_libdir}/qml/org/kde/plasma/networkmanagement
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
%setup -q -n plasma-nm-%{version}

%build
%cmake
%make

%install
%makeinstall_std -C build

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

