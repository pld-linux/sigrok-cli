Summary:	Basic hardware access for logic analyzers - command line tool
Summary(pl.UTF-8):	Podstawowy dostęp do sprzętu dla analizatorów logicznych - narzędzie linii poleceń
Name:		sigrok-cli
Version:	0.7.0
Release:	1
License:	GPL v3+
Group:		Applications/Science
Source0:	http://www.sigrok.org/download/source/sigrok-cli/%{name}-%{version}.tar.gz
# Source0-md5:	77cb745e2fa239c7bd1ea81e2d67ede9
URL:		http://www.sigrok.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	libsigrok-devel >= 0.5.0
BuildRequires:	libsigrokdecode-devel >= 0.5.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.22
Requires:	glib2 >= 1:2.32.0
Requires:	libsigrok >= 0.5.0
Requires:	libsigrokdecode >= 0.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sigrok-cli is a command-line tool written in C, which uses both
libsigrok and libsigrokdecode to provide the basic sigrok
functionality from the command-line. Among other things, it is useful
for scripting purposes.

%description -l pl.UTF-8
sigrok-cli to napisane w C narzędzie linii poleceń, wykorzystujące
biblioteki libsigrok oraz libsigrokdecode dla zapewnienia podstawowej
funkcjonalności sigrok z linii poleceń. Jest przydatne między innymi
do tworzenia skryptów.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/sigrok-cli
%{_mandir}/man1/sigrok-cli.1*
