Summary:	MP4v2 library provides api for creation and modification of MP4 files
Name:		mp4v2
Version:	1.9.1
Release:	0.1
License:	MPL v1.1
Group:		Libraries
Source0:	http://mp4v2.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	986701929ef15b03155ac4fb16444797
URL:		http://code.google.com/p/mp4v2/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MP4v2 library provides an API to create and modify mp4 files as
defined by ISO-IEC:14496-1:2001 MPEG-4 Systems. This file format is
derived from Apple's QuickTime file format that has been used as a
multimedia file format in a variety of platforms and applications. It
is a very powerful and extensible format that can accomodate
practically any type of media.

%package devel
Summary:	Header files for MP4v2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for MP4v2.

%package static
Summary:	Static MP4v2 library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of MP4v2.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_bindir}/mp4track
%attr(755,root,root) %{_bindir}/mp4extract
%attr(755,root,root) %{_bindir}/mp4trackdump
%attr(755,root,root) %{_bindir}/mp4art
%attr(755,root,root) %{_bindir}/mp4tags
%attr(755,root,root) %{_bindir}/mp4subtitle
%attr(755,root,root) %{_bindir}/mp4chaps
%attr(755,root,root) %{_bindir}/mp4info
%attr(755,root,root) %{_bindir}/mp4file
%attr(755,root,root) %{_libdir}/libmp4v2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmp4v2.so.?
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmp4v2.so
%{_includedir}/mp4v2

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmp4v2.a
