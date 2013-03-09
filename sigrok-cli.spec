%define	snap	5d09b45
Summary:	Basic hardware access drivers for logic analyzers
Name:		sigrok-cli
Version:	0.3.1
Release:	0.%{snap}.1
License:	GPL v3+
Group:		X11/Applications/Science
URL:		http://www.sigrok.org/
# Source0:	http://downloads.sourceforge.net/sigrok/%{name}-%{version}.tar.gz
# Source0:	http://sigrok.org/gitweb/?p=sigrok-cli.git;a=snapshot;h=%{snap};sf=tgz;/%{name}-%{snap}.tar.gz
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	f9bf44dac11d6cc7ebd040a76381d831
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	glib2-devel
BuildRequires:	libsigrok-devel >= 0.2.0
BuildRequires:	libsigrokdecode-devel

%description
%{name} is a command-line tool written in C, which uses both libsigrok
and libsigrokdecode to provide the basic sigrok functionality from the
command-line. Among other things, it is useful for scripting purposes.

%prep
%setup -q -n %{name}-%{snap}

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
