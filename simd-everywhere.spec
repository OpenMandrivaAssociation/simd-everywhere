%if "%{_build_cpu}" == "aarch64"
%global optflags %{optflags} -march=armv8+crc
%endif

Name:		simd-everywhere
Version:	0.8.2
Release:	1
Source0:	https://github.com/simd-everywhere/simde/archive/refs/tags/v%{version}.tar.gz
Summary:	Headers-only library for cross-platform SIMD instructions
URL:		https://github.com/simd-everywhere/simde
License:	GPL
Group:		Development/C
BuildArch:	noarch
BuildRequires:	meson
BuildSystem:	meson

%description
Headers-only library for cross-platform SIMD instructions

%install -a
# The pkgconfig files aren't in the right place for a noarch package
mkdir -p %{buildroot}%{_datadir}
mv %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_datadir}
rmdir %{buildroot}%{_libdir}

%files
%{_includedir}/simde
%{_datadir}/pkgconfig/*
