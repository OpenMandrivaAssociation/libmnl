# libmnl is used by libnetfilter_conntrack
# libnetfilter_conntrack is used by iptables
# iptables is used by systemd
# libsystemd is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 0
%define libname %mklibname mnl %{major}
%define devname %mklibname mnl -d
%define lib32name libmnl%{major}
%define dev32name libmnl-devel

Summary:	Minimalistic Netlink communication library
Name:		libmnl
Version:	1.0.5
Release:	1
License:	LGPLv2+
Group:		System/Kernel and hardware
Url:		http://netfilter.org/projects/libmnl/
Source0:	http://netfilter.org/projects/libmnl/files/%{name}-%{version}.tar.bz2
BuildRequires:	kernel-headers

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

%if %{with compat32}
%package -n %{lib32name}
Summary:	Minimalistic Netlink communication library (32-bit)
Group:		System/Libraries
BuildRequires:	libc6
Requires:	libc6

%description -n %{lib32name}
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong. This
library aims to provide simple helpers that allows you to re-use code and to
avoid re-inventing the wheel.

%package -n %{dev32name}
Summary:	Development files for libmnl (32-bit)
Group:		Development/C
Requires:	%{lib32name} = %{EVRD}
Requires:	%{devname} = %{EVRD}

%description -n %{dev32name}
This package includes the development files for %{name}.
%endif

%prep
%autosetup -p1

export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

# clang doesnt like the visibility definitions in this code
export CFLAGS="%{optflags} -fvisibility=default"
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libmnl.so.%{major}*

%files -n %{devname}
%{_includedir}/libmnl
%{_libdir}/libmnl.so
%{_libdir}/pkgconfig/libmnl.pc

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libmnl.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libmnl.so
%{_prefix}/lib/pkgconfig/libmnl.pc
%endif
