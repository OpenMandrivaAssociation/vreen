%define git 20131027

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Qt wrapper library for vk.com API
Name:		vreen
# From CMakeLists.txt
Version:	0.9.5
Release:	0.%{git}.4
License:	LGPLv3+
Group:		System/Libraries
Url:		http://github.com/gorthauer/vreen
# From git
Source0:	vreen-%{git}.tar.bz2
Patch0:		vreen-audio-api.patch
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(QtWebKit)

%description
Qt wrapper library for VKontakte social network (vk.com) API.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Qt wrapper library for vk.com API
Group:		System/Libraries

%description -n %{libname}
Qt wrapper library for VKontakte social network (vk.com) API.

%files -n %{libname}
%doc AUTHORS
%{_libdir}/libvreen.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for vk.com API Qt wrapper library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for vreen library.

%files -n %{devname}
%{_includedir}/vreen
%{_libdir}/libvreen.so
%{_libdir}/libvreenoauth.a
%{_libdir}/pkgconfig/vreen.pc
%{_libdir}/pkgconfig/vreenoauth.pc

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{git}
%patch0 -p1

%build
export CXX=g++
%cmake_qt4 \
	-DVREEN_WITH_QMLAPI=OFF
%make

%install
%makeinstall_std -C build

