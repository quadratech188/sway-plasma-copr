%global forgeurl https://github.com/quadratech188/sway-plasma

Name: sway-plasma
Version: 0.1.3
Release: %autorelease
Summary: Sway patched to run KDE Plasma

%{forgemeta}
License: MIT
URL: %{forgeurl}
Source0: %{forgesource}

BuildRequires: gcc
BuildRequires: git
BuildRequires: meson

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(json-c) >= 0.13
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(libinput) >= 1.26.0
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(libsystemd) >= 239
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-server)
# BuildRequires: pkgconfig(wlroots-0.20)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xkbcommon)

# etc
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: g++
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(Plasma)
BuildRequires: cmake(Qt6Qml)

# wlroots
BuildRequires: glslang
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gbm) >= 21.1
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(hwdata)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libdisplay-info) >= 0.2.0
BuildRequires: pkgconfig(libdrm) >= 2.4.129
BuildRequires: pkgconfig(libinput) >= 1.21.0
BuildRequires: pkgconfig(libliftoff)
BuildRequires: pkgconfig(libseat)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(pixman-1) >= 0.46.0
BuildRequires: pkgconfig(vulkan) >= 1.2.182
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols) >= 1.47
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server) >= 1.24.0
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-composite)
BuildRequires: pkgconfig(xcb-dri3)
BuildRequires: pkgconfig(xcb-errors)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-present)
BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-res)
BuildRequires: pkgconfig(xcb-shm)
BuildRequires: pkgconfig(xcb-xfixes) >= 1.15
BuildRequires: pkgconfig(xcb-xinput)
BuildRequires: pkgconfig(xkbcommon) >= 1.8.0
BuildRequires: pkgconfig(xwayland)

%description
Sway patched to run KDE Plasma

%prep
%forgeautosetup -p1

%build

%meson \
	--wrap-mode=nofallback \
	--force-fallback-for=wlroots \
	-Dtray=disabled \
	-Dwlroots:default_library=static
%meson_build

cd etc
%cmake_kf6
%cmake_build

%install
%meson_install --skip-subprojects=wlroots

cd etc
%cmake_install

%files
%license LICENSE
%{_bindir}/start-sway-plasma
%{_bindir}/sway-plasma
%{_datadir}/sway-plasma
%{_datadir}/wayland-sessions/sway-plasma.desktop
%{_datadir}/xdg-desktop-portal/sway-plasma-portals.conf
%{_kf6_qmldir}/com/github/quadratech188/swaystate
%{_kf6_qtplugindir}/plasma/applets/com.github.quadratech188*
%{_libexecdir}/sway-plasma
%{_mandir}/man1/sway*
%{_sysconfdir}/sway-plasma

%changelog
%autochangelog
