#
# Conditional build:
%bcond_with	tests	# do perform "make test"
#		(fails probably because of libmad version different from reference one)

%define		pdir	Audio
%define		pnam	MPEG
Summary:	Audio::MPEG Perl module - encoding and decoding of MPEG Audio
Summary(pl.UTF-8):	Moduł Perla Audio::MPEG - kodowanie i dekodowanie dźwięku MPEG
Name:		perl-Audio-MPEG
Version:	0.04
Release:	5
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9c5b09cf06c934a001b81c05f786a295
Patch0:		%{name}-lame-fix.patch
Patch1:		%{name}-build.patch
URL:		http://search.cpan.org/dist/Audio-MPEG/
BuildRequires:	lame-libs-devel
BuildRequires:	libmad-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will allow a Perl program to verify an MP3 file (fixed and
variable bitrate), decode it into a high-resolution (24 bit) PCM
stream, apply filtering effects to the data (stereo->mono, fade
in/out, equalizer), transform that stream into an audio stream (WAV,
Sun AU, integer PCM, floating point PCM), and finally encode a PCM
stream as an MP3.

%description -l pl.UTF-8
Ten moduł umożliwia programom w Perlu weryfikację plików MP3 (o
zmiennej i stałej prędkości strumienia), dekodowanie ich do strumienia
PCM o dużej rozdzielczości (24 bity), przepuszczanie przez filtry
efektów (stereo->moni, wchodzenie/wyciszanie, equalizer),
przekształcanie tego strumienia na strumień dźwiękowy (WAV, Sun AU,
całkowitoliczbowy PCM, zmiennoprzecinkowy PCM) i w końcu kodowanie
strumieni PCM do MP3.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

# "encode" tests and half of "wave" test fail
# please, check it again
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Audio/MPEG.pm
%dir %{perl_vendorarch}/auto/Audio/MPEG
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/MPEG/*.so
%{_mandir}/man3/*
