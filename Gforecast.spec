Summary:	A weather forecasting applet for the GNOME Panel
Summary(pl):	Applet dla GNOME pokazuj±cy pogodê w danym regionie
Name:		Gforecast
Version:	0.4
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/waepplets/%{name}-%{version}.tar.gz
# Source0-md5:	c0f582ea548a3be3f46d7acb8249baa3
Patch0:		%{name}-configure.in.patch
URL:		http://waepplets.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-core-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
Simple applet that gets the forecast for a chosen city and shows it as
an icon image in a GNOME applet.

%description -l pl
Prosty applet, który pobiera informacjê o pogodzie dla danego miasta i
wy¶wietla j± w formie ikony.

%prep
%setup -q
%patch0 -p1

%build
rm -rf missing
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_datadir}/applets/Monitors/*
%{_pixmapsdir}/*
