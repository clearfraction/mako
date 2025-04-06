Name     : mako
Version  : 1.10.0
Release  : 1
URL      : https://github.com/emersion/mako
Source0  : https://github.com/emersion/mako/archive/refs/tags/v%{version}.tar.gz
Summary  : Lightweight Wayland notification daemon
Group    : Development/Tools
License  : MIT
BuildRequires : meson
BuildRequires : gcc
BuildRequires : wayland-dev wayland-protocols-dev
BuildRequires : pango-dev
BuildRequires : systemd-dev


%description
Lightweight Wayland notification daemon


%prep
%setup -q

%build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fzero-call-used-regs=used -mprefer-vector-width=256  "
export FCFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fzero-call-used-regs=used -mprefer-vector-width=256  "
export FFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fzero-call-used-regs=used -mprefer-vector-width=256  "
export CXXFLAGS="$CXXFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fzero-call-used-regs=used -mprefer-vector-width=256  "
meson \
    --libdir=lib64 --prefix=/usr \
    --buildtype=plain -Dman-pages=disabled builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
/usr/bin/mako
/usr/bin/makoctl
/usr/share/dbus-1/services/fr.emersion.mako.service
