Summary:	Basic hardware access drivers for logic analyzers
Name:		sigrok-cli
Version:	0.3.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Science
URL:		http://www.sigrok.org/
Source0:	http://downloads.sourceforge.net/sigrok/%{name}-%{version}.tar.gz
# Source0-md5:	eed06b1408a969b86b0f6e1aa29ae0cb
BuildRequires:	glib2-devel
BuildRequires:	libsigrok-devel
BuildRequires:	libsigrokdecode-devel

%description
%{name} is a command-line tool written in C, which uses both libsigrok
and libsigrokdecode to provide the basic sigrok functionality from the
command-line. Among other things, it is useful for scripting purposes.

%prep
%setup -q

%build
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
