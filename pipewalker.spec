Summary:	Simple logic game
Summary(pl.UTF-8):	Prosta gra logiczna
Name:		pipewalker
Version:	0.8.2
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/pipewalker/%{name}-%{version}-src.tar.gz
# Source0-md5:	8dfde48844d85208fc6a580062f9c2a1
Patch0:		%{name}-desktop.patch
URL:		http://pipewalker.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a puzzle game where pieces of a computer network are to be
turned in the right/left direction to make all computers connected to
the same network. This game is clone of NetWalk.

%description -l pl.UTF-8
Prosta gra logiczna, w której elementy sieci komputerowej należy
obracać w lewo/prawo w celu podłączenia wszystkich komputerów do tej
samej sieci. Gra jest klonem gry NetWalk.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/pipewalker
%{_datadir}/games/pipewalker
%{_desktopdir}/pipewalker.desktop
%{_pixmapsdir}/pipewalker.xpm
