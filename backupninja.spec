%define name    backupninja
%define version 1.0.1

Summary:    Backupninja backup tool
Name:       %{name}
Version:    %{version}
Release:    1
License:    GPL
Group:      Applications/System
URL:        https://labs.riseup.net/code/projects/show/backupninja
Source:     %{name}-%{version}.tar.gz
Requires:   bash, gawk, rdiff-backup, gzip
Provides:   %{name}
Packager:   Petr Klima <Petr.Klima@madeta-group.cz>
BuildRoot:  %{_tmppath}/%{name}-%{version}
Prefix:     %{_prefix}

%description
Modular rdiff.backup tool

%prep
%setup -q

%build
%configure
make

%install
rm -rf ${buildroot}
%makeinstall
mkdir -p "%{buildroot}%{_sysconfdir}/backup.d"
mkdir -p "%{buildroot}%{_localstatedir}/backups"
mkdir -p "%{buildroot}%{_localstatedir}/log"
touch "%{buildroot}%{_localstatedir}/log/backupninja.log"

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/*
%{_datadir}/backupninja/*
%{_libdir}/backupninja/*

%config %{_sysconfdir}/cron.d/backupninja
%config %{_sysconfdir}/logrotate.d/backupninja

%config(noreplace) %{_sysconfdir}/backupninja.conf
%dir %{_localstatedir}/backups

%ghost %{_localstatedir}/log/backupninja.log

%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_mandir}/man1/*
%{_mandir}/man5/*

%defattr(0640,root,root,0750)
%dir %{_sysconfdir}/backup.d


%changelog
* Sun Oct 14 2007 Adam Monsen <haircut@gmail.com> 0.9.5-1
- use cleanup steps during %install and %clean
* Mon Apr 29 2002 Petr Klima <Petr.Klima@madeta-group.cz> 0.7.0
- first RPM release
