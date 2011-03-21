%define	major 0
%define libname %mklibname mnl %{major}
%define develname %mklibname mnl -d

Summary:	Minimalistic Netlink communication library
Name:		libmnl
Version:	1.0.1
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Kernel and hardware
URL:		http://netfilter.org/projects/libmnl/
Source0:	http://netfilter.org/projects/libmnl/files/%name-%version.tar.bz2
Source1:	http://netfilter.org/projects/libmnl/files/%name-%version.tar.bz2.sig
BuildRequires:	linux-userspace-headers
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong. This
library aims to provide simple helpers that allows you to re-use code and to
avoid re-inventing the wheel.

%package -n	%{libname}
Summary:	Minimalistic Netlink communication library
Group:		System/Libraries

%description -n	%{libname}
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong. This
library aims to provide simple helpers that allows you to re-use code and to
avoid re-inventing the wheel.

%package -n	%{develname}
Summary:	Development files for libmnl
Group:		Development/C

%description -n	%{develname}
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong. This
library aims to provide simple helpers that allows you to re-use code and to
avoid re-inventing the wheel.

%prep

%setup -q

%build
rm -Rf autom4te.cache
aclocal -I m4
autoreconf -fi

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -f %{buildroot}%{_libdir}/*.la

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

