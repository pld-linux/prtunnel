Summary:	Tunneling a TCP connection through to a remote server using an HTTP or SOCKS5 proxy
Summary(pl):	Tunelowanie po³±czenia TCP do zdalnego serwera przy u¿yciu proxy HTTP lub SOCKS5
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

- tunneling TCP connections from client programs to a remote server
  through an HTTP or SOCKS5 proxy (useful if you're behind such a
  proxy and want to use a program that doesn't have native proxy
  support),
- tunneling TCP connections from SOCKS-capable client programs through
  an HTTP or SOCKS5 proxy
- tunneling TCP connections from an IPv4 client program to an IPv6
  server and vice-versa,
- forwarding TCP connections,
- running as a simple SOCKS proxy server.

%description -l pl
prtunnel to program tuneluj±cy po³±czenia TCP/IP na wiele ró¿nych
sposobów, m.in. przez serwery proxy HTTP i SOCKS5. Mo¿liwe
zastosowania obejmuj±:

- tunelowanie po³±czeñ TCP z programów klienckich do zdalnego serwera
  poprzez proxy HTTP lub SOCKS5 (przydatne kiedy jeste¶my za takim
  proxy i chcemy u¿yæ programu nie obs³uguj±cego natywnie proxy),
- tunelowanie po³±czeñ TCP z programów klienckich obs³uguj±cych SOCKS
  przez proxy HTTP lub SOCKS5,
- tunelowanie po³±czeñ TCP z programów klienckich IPv4 do serwerów
  IPv6 i na odwrót,
- przekazywanie po³±czeñ TCP,
- uruchamianie prostego serwera proxy SOCKS.

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
