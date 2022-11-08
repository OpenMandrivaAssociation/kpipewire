%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define libname %mklibname KPipeWire
%define devname %mklibname -d KPipeWire

Summary:	Library for working with PipeWire
Name:		kpipewire
Version:	5.26.3
Release:	1
License:	LGPL
Group:		System/Libraries
Url:		http://kde.org/
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(QtWaylandScanner)
BuildRequires:	cmake(WaylandScanner)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	cmake(PlasmaWaylandProtocols) >= 1.4.0
BuildRequires:	pkgconfig(Qt5WaylandClient)
BuildRequires:	qt5-qtwayland
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(epoxy)
BuildRequires:	pkgconfig(libdrm)
# For qch docs
BuildRequires:	doxygen
BuildRequires:	qt5-assistant

%description
Libraries for working with PipeWire

%package -n %{libname}
Summary:	Libraries for working with PipeWire
Group:		System/Libraries

%description -n %{libname}
Libraries for working with PipeWire

%files -n %{libname} -f kpipewire5.lang
%{_libdir}/libKPipeWire.so.*
%{_libdir}/libKPipeWireRecord.so.*
%{_libdir}/qt5/qml/org/kde/pipewire
%{_datadir}/qlogging-categories5/*.categories

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/KPipeWire
%{_libdir}/cmake/KPipeWire
%{_libdir}/libKPipeWire.so
%{_libdir}/libKPipeWireRecord.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kpipewire5
