%define major 0
%define libname %mklibname mnl %{major}
%define devname %mklibname mnl -d

# clang doesnt like the visibility definitions in this code
%global optflags %{optflags} -Oz -fvisibility=default

Summary:	Minimalistic Netlink communication library
Name:		libmnl
Version:	1.0.5
Release:	2
License:	LGPLv2+
Group:		System/Kernel and hardware
Url:		https://netfilter.org/projects/libmnl/
Source0:	http://netfilter.org/projects/libmnl/files/%{name}-%{version}.tar.bz2
BuildRequires:	kernel-headers
Obsoletes:	libmnl0 < 1.0.5-2
Obsoletes:	libmnl-devel < 1.0.5-2

%description
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong. This
library aims to provide simple helpers that allows you to re-use code and to
avoid re-inventing the wheel.

%package -n %{libname}
Summary:	Minimalistic Netlink communication library
Group:		System/Libraries

%description -n %{libname}
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong. This
library aims to provide simple helpers that allows you to re-use code and to
avoid re-inventing the wheel.

%package -n %{devname}
Summary:	Development files for libmnl
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	mnl-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libmnl.so.%{major}*

%files -n %{devname}
%{_includedir}/libmnl
%{_libdir}/libmnl.so
%{_libdir}/pkgconfig/libmnl.pc
