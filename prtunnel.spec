Summary:	prtunnel tunnels a TCP connection through to a remote server using an HTTP or SOCKS5 proxy
Name:		prtunnel
Version:	0.2.2
Release:	0.1
License:	GPL
Group:		Daemons
Source0:	http://www.joshbeam.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	42d6a81a6bf7fe4500a235e7659dba8c
URL:		http://www.joshbeam.com/software/prtunnel.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
prtunnel is a program that can tunnel TCP/IP connections in a variety
of ways, including through HTTP and SOCKS5 proxy servers. Some if its
possible uses include:

Tunneling TCP connections from client programs to a remote server
through an HTTP or SOCKS5 proxy (useful if you're behind such a proxy
and want to use a program that doesn't have native proxy support)
Tunneling TCP connections from SOCKS-capable client programs through
an HTTP or SOCKS5 proxy Tunneling TCP connections from an IPv4 client
program to an IPv6 server and vice-versa Forwarding TCP connections
Running as a simple SOCKS proxy server

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D prtunnel $RPM_BUILD_ROOT%{_bindir}/prtunnel
install -D prtunnel.1 $RPM_BUILD_ROOT%{_mandir}/man1/prtunnel.1

%clean
rm -fR $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
