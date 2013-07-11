Summary:	Basic hardware access drivers for logic analyzers
Name:		sigrok-cli
Version:	0.4.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Science
URL:		http://www.sigrok.org/
Source0:	http://www.sigrok.org/download/source/sigrok-cli/%{name}-%{version}.tar.gz
# Source0-md5:	7495ac50869f8418ab1b8d68120fd383
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	libsigrok-devel >= 0.2.0-1
BuildRequires:	libsigrokdecode-devel >= 0.2.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{name} is a command-line tool written in C, which uses both libsigrok
and libsigrokdecode to provide the basic sigrok functionality from the
command-line. Among other things, it is useful for scripting purposes.

%prep
%setup -q

%build
install -d autostuff
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
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
%attr(755,root,root) %{_bindir}/sigrok-cli
%{_mandir}/man1/sigrok-cli.1*
