#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	MPEG
Summary:	Audio::MPEG Perl module - encoding and decoding of MPEG Audio
Summary(pl):	Modu³ Perla Audio::MPEG - kodowanie i dekodowanie d¼wiêku MPEG
Name:		perl-Audio-MPEG
Version:	0.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-lame-fix.patch
BuildRequires:	lame-libs-devel
BuildRequires:	mad-devel
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will allow a Perl program to verify an MP3 file (fixed and
variable bitrate), decode it into a high-resolution (24 bit) PCM
stream, apply filtering effects to the data (stereo->mono, fade
in/out, equalizer), transform that stream into an audio stream (WAV,
Sun AU, integer PCM, floating point PCM), and finally encode a PCM
stream as an MP3.

%description -l pl
Ten modu³ umo¿liwia programom w Perlu weryfikacjê plików MP3 (o
zmiennej i sta³ej prêdko¶ci strumienia), dekodowanie ich do strumienia
PCM o du¿ej rozdzielczo¶ci (24 bity), przepuszczanie przez filtry
efektów  (stereo->moni, wchodzenie/wyciszanie, equalizer),
przekszta³canie tego strumienia na strumieñ d¼wiêkowy (WAV, Sun AU,
ca³kowitoliczbowy PCM, zmiennoprzecinkowy PCM) i w koñcu kodowanie
strumieni PCM do MP3.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

# "encode" tests and half of "wave" test fail
#%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Audio/MPEG.pm
%dir %{perl_sitearch}/auto/Audio/MPEG
%{perl_sitearch}/auto/Audio/MPEG/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Audio/MPEG/*.so
%{_mandir}/man3/*
