Summary: A weather forecasting applet for the GNOME Panel
Name: Gforecast
Version: 0.1
Release: 1
Copyright: GPL
Group: User Interface/Desktops
Source: Gforecast-0.1.tar.gz
Requires: gnome-libs >= 1.2.1
Requires: gnome-core >= 1.2.1
URL: http://waepplets.sourceforge.net/
BuildRoot: /tmp/Gforecast-root

%description
Simple applet that gets the forecast for a chosen city and shows it as
an icon image in a GNOME applet.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install
du -k $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
/usr/bin/*
/usr/share/applets/*
/usr/etc/CORBA/servers/*
