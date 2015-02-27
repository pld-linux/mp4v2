Summary:	MP4v2 library provides API for creation and modification of MP4 files
Summary(pl.UTF-8):	Biblioteka MP4v2 - API do tworzenia i modyfikowania plików MP4
Name:		mp4v2
Version:	2.0.0
Release:	3
License:	MPL v1.1
Group:		Applications/Multimedia
#Source0Download: http://code.google.com/p/mp4v2/downloads/list
Source0:	http://mp4v2.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	c91f06711225b34b4c192c9114887b14
Patch0:		%{name}-export.patch
URL:		http://code.google.com/p/mp4v2/
BuildRequires:	help2man
BuildRequires:	libstdc++-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MP4v2 library provides an API to create and modify MP4 files as
defined by ISO-IEC:14496-1:2001 MPEG-4 Systems. This file format is
derived from Apple's QuickTime file format that has been used as a
multimedia file format in a variety of platforms and applications. It
is a very powerful and extensible format that can accommodate
practically any type of media.

%description -l pl.UTF-8
Biblioteka MP4v2 udostępnia API do tworzenia i modyfikowania plików
MP4 zgodnych z definicją ISO-IEC:14496-1:2001 MPEG-4 Systems. Ten
format plików wywodzi się z formatu Apple QuickTime, używanego przez
wiele platform i aplikacji jako format plików multimedialnych. Jest to
format mający duże możliwości i rozszerzalny, mogący pomieścić
praktycznie każdy rodzaj obiektu multimedialnego.

%package libs
Summary:	Shared MP4v2 library
Summary(pl.UTF-8):	Biblioteka współdzielona MP4v2
Group:		Libraries
Conflicts:	mp4v2 < 1.9.1-2

%description libs
The libmp4v2 library provides an abstraction layer for working with
files using the mp4 container format.

%description libs -l pl.UTF-8
Biblioteka libmp4v2 zapewnia warstwę abstrakcji do pracy z plikami
wykorzystującymi format kontenera mp4.

%package devel
Summary:	Header files for MP4v2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki MP4v2
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for MP4v2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki MP4v2.

%package static
Summary:	Static MP4v2 library
Summary(pl.UTF-8):	Statyczna biblioteka MP4v2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of MP4v2.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki MP4v2.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

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
%{_mandir}/man1/mp4art.1*
%{_mandir}/man1/mp4file.1*
%{_mandir}/man1/mp4subtitle.1*
%{_mandir}/man1/mp4track.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmp4v2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmp4v2.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmp4v2.so
%{_libdir}/libmp4v2.la
%{_includedir}/mp4v2

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmp4v2.a
