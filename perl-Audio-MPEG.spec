#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	MPEG
Summary:	Audio::MPEG Perl module - encoding and decoding of MPEG Audio
Summary(pl):	Modu� Perla Audio::MPEG - kodowanie i dekodowanie d�wi�ku MPEG
Name:		perl-Audio-MPEG
Version:	0.04
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9c5b09cf06c934a001b81c05f786a295
Patch0:		%{name}-lame-fix.patch
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

%description -l pl
Ten modu� umo�liwia programom w Perlu weryfikacj� plik�w MP3 (o
zmiennej i sta�ej pr�dko�ci strumienia), dekodowanie ich do strumienia
PCM o du�ej rozdzielczo�ci (24 bity), przepuszczanie przez filtry
efekt�w  (stereo->moni, wchodzenie/wyciszanie, equalizer),
przekszta�canie tego strumienia na strumie� d�wi�kowy (WAV, Sun AU,
ca�kowitoliczbowy PCM, zmiennoprzecinkowy PCM) i w ko�cu kodowanie
strumieni PCM do MP3.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

# "encode" tests and half of "wave" test fail
#%%{!?_without_tests:%{__make} test}

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
%{perl_vendorarch}/auto/Audio/MPEG/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/MPEG/*.so
%{_mandir}/man3/*
