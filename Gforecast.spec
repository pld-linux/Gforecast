Summary:	A weather forecasting applet for the GNOME Panel
Summary(pl):	Applet dla GNOME pokazuj±cy pogodê w danym regionie
Name:		Gforecast
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://download.sourceforge.net/pub/sourceforge/waepplets/%{name}-%{version}.tar.gz
URL:		http://waepplets.sourceforge.net/
BuildRequires:	gnome-core-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
Simple applet that gets the forecast for a chosen city and shows it as
an icon image in a GNOME applet.

%description -l pl
Prosty applet, który pobiera informacjê o pogodzie dla danego miasta
i wy¶wietla j± w formie ikony.

%prep
%setup -q

%build
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_datadir}/applets/Monitors/*
%{_pixmapsdir}/*
