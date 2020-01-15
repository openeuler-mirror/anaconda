%define livearches %{ix86} x86_64
%define _empty_manifest_terminate_build 0

Name:		anaconda
Version:	29.24.7
Release:	21
Summary:	Graphical system installer
License:	GPLv2+ and MIT
URL:		https://fedoraproject.org/wiki/Anaconda
Source0:	%{name}-%{version}.tar.bz2

Patch6000:      anaconda-change-log-localtime-to-gmtime.patch
Patch6001:      bugfix-Increase-network-timeout-constant.patch
Patch6002:      bugfix-Set-timeout-for-all-session.get-calls.patch
Patch6003:      anaconda-not-acquire-the-lock-of-imp.patch

Patch9000:      bugfix-update-network-and-hostname-translation.patch
Patch9001:      add-password-policy.patch
Patch9002:      bugfix-add-check-url-while-no-network.patch
Patch9003:      anaconda-fix-hostname-info.patch
Patch9004:      add-openEuler-password-policy.patch
Patch9005:      anaconda-prohibit-press-done-twice.patch
Patch9006:      change_passwd_min_length_to_8.patch
Patch9007:      bugfix-fix-data-encrypt-weak-passphrase-save.patch
Patch9008:      bugfix-disable-set-password-without-confirmation.patch
Patch9009:      bugfix-set-right-eula-location.patch
Patch9010:      bugfix-aarch64-anaconda-do-not-use-console.patch
Patch9011:      bugfix-x86-bootloader-install-fail.patch
Patch9012:      force-set-root-password.patch
Patch9013:      anaconda-fix-logo-display-in-low-screen-resolution.patch
Patch9014:      anaconda-fix-rnotes-display-in-low-screen-resolution.patch
Patch9015:      anaconda-make-name-not-force-to-uppercase.patch
Patch9016:      anaconda-add-moreos-install-class.patch
Patch9017:      anaconda-fix-password-expired.patch
Patch9018:      anaconda-fix-GUI-nfs-unknown-error.patch
Patch9019:      anaconda-change-topbar-background-size.patch
Patch9020:      anaconda-hide-help-button.patch
Patch9021:      anaconda-add-quiet-cmdline-args-for-x86.patch
Patch9022:	anaconda-modify-interface-is-extended-in-Chinese-mod.patch
Patch9023:      bugfix-fix-vender-issue.patch 
Patch9024:      bugfix-disable-adding-virtual-device-in-network-spokes.patch
Patch9025:      bugfix-for-encrypting-partion.patch
Patch9026:      bugfix-modify-arguments-parsing.patch
Patch9027:      anaconda-add-boot-options-for-raid-3408.patch
Patch9028:      anaconda-add-kdump-parameter-into-kernel-cmdline.patch

BuildRequires:	audit-libs-devel libtool gettext-devel >= 0.19.8 gtk3-devel >= 3.22.17
BuildRequires:  gtk-doc gtk3-devel-docs >= 3.22.17 glib2-doc gobject-introspection-devel
BuildRequires:  glade-devel libgnomekbd-devel libxklavier-devel >= 5.4 pango-devel
BuildRequires:  python3-kickstart >= 3.16-1 python3-devel python3-nose systemd 
BuildRequires:  rpm-devel >= 4.10.0 libarchive-devel >= 3.0.4 gdk-pixbuf2-devel
BuildRequires:  libtimezonemap-devel >= 0.4.1-2 libxml2 

Requires:       anaconda-core = %{version}-%{release}
Requires:       anaconda-tui = %{version}-%{release}
Requires:       udisks2-iscsi libblockdev-plugins-all realmd isomd5sum kexec-tools
Requires:       createrepo_c tmux gdb rsync python3-meh-gui adwaita-icon-theme dracut-live
Requires:       tigervnc-server-minimal libxklavier libgnomekbd libtimezonemap xz
Requires:       nm-connection-editor keybinder3 anaconda-user-help yelp system-logos
Requires:       blivet-gui-runtime python3 dracut dracut-network python3-kickstart

%ifarch %livearches
BuildRequires:  desktop-file-utils 
Requires:       zenity fcoe-utils
%endif

Provides:       anaconda-gui = %{version}-%{release}
Obsoletes:      anaconda-gui < %{version}-%{release}

Provides:       anaconda-widgets = %{version}-%{release}
Obsoletes:      anaconda-widgets < %{version}-%{release}

Provides:       anaconda-dracut = %{version}-%{release}
Obsoletes:      anaconda-dracut < %{version}-%{release} 

Provides:       anaconda-install-env-deps = %{version}-%{release} 
Obsoletes:      anaconda-install-env-deps < %{version}-%{release}

%description
The 'anaconda' dracut module handles installer-specific boot tasks and
options. This includes driver disks, kickstarts, and finding the anaconda
runtime on NFS/HTTP/FTP servers or local disks.

%package        core
Summary:        Core of the Anaconda installer
Requires:       python3-libs python3-dnf >= 3.6.0 python3-blivet >= 1:3.1.0-1
Requires:       python3-blockdev >= 2.1 rpm-python3 >= 4.10.0 python3-productmd
Requires:       libreport-anaconda >= 2.0.21-1 libselinux-python3 python3-meh >= 0.23-1
Requires:       python3-pyparted >= 2.5-2 python3-requests python3-requests-file
Requires:       python3-requests-ftp python3-kickstart langtable-data >= 0.0.34
Requires:       langtable-python3 >= 0.0.34 util-linux >= 2.15.1 python3-gobject-base
Requires:       python3-dbus python3-pwquality python3-systemd python3-pydbus 
Requires:       cracklib-dicts python3-pytz teamd NetworkManager NetworkManager-libnm
Requires:       dhclient kbd chrony python3-ntplib systemd python3-pid 
Requires:       python3-ordered-set >= 2.0.0 python3-coverage glibc-langpack-en 
Requires:       anaconda-tui = %{version}-%{release}

Provides:       anaconda-images = %{version}-%{release}
Obsoletes:      anaconda-images < %{version}-%{release}

Provides:       anaconda-runtime = %{version}-%{release} 
Obsoletes:      anaconda-runtime < %{version}-%{release}
Obsoletes:      booty <= 0.107-1

%ifarch %livearches
Requires:       usermode
%endif

%description    core
The anaconda-core package contains the program which was used to install your
system.

%package        tui
Summary:        Textual user interface for the Anaconda installer
Requires:       anaconda-core = %{version}-%{release} python3-simpleline

%description    tui
This package contains textual user interface for the Anaconda installer.

%package        devel
Summary:        Header files for anaconda
Requires:       glade %{name} = %{version}-%{release}
Provides:       anaconda-widgets-devel = %{version}-%{release}
Obsoletes:      anaconda-widgets-devel < %{version}-%{release}

%description    devel
Header files for anaconda

%prep
%autosetup -n %{name}-%{version} -p1

cd pyanaconda/installclasses
sed -i "s/more_os_name/%{efi_vendor}/g" more_os_name.py
mv more_os_name.py %{efi_vendor}.py

%build
%configure ANACONDA_RELEASE=%{release}
%make_build

%install
%make_install
%delete_la

install -d -m 0755 %{buildroot}%{_datadir}/anaconda/addons

%ifarch %livearches
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/liveinst.desktop
%endif

%ldconfig_scriptlets

%ifarch %livearches
%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
%endif

%files
%defattr(-,root,root)
%doc README
%license COPYING
%{_libdir}/libAnacondaWidgets.so.*
%{_libdir}/girepository*/AnacondaWidgets*typelib
%{python3_sitearch}/gi/overrides/*
%{python3_sitearch}/pyanaconda/ui/gui/*
%{_prefix}/libexec/anaconda/dd_*
%{_prefix}/lib/dracut/modules.d/80%{name}/*

%files        core
%defattr(-,root,root)
%doc README 
%license COPYING
%{_sbindir}/anaconda
%{_sbindir}/handle-sshpw
%{_bindir}/instperf
%{_bindir}/analog
%{_bindir}/anaconda-cleanup
%{_bindir}/anaconda-disable-nm-ibft-plugin
%{_libdir}/libAnacondaWidgets.so
%{_prefix}/libexec/anaconda
%{_prefix}/lib/systemd/system-generators/*
%{_unitdir}/*
%{_datadir}/anaconda
%{_datadir}/locale/*
%{python3_sitearch}/pyanaconda
%exclude %{_prefix}/libexec/anaconda/dd_*
%exclude %{_libdir}/libAnacondaWidgets.so
%exclude %{_datadir}/gtk-doc
%exclude %{_datadir}/glade/catalogs/AnacondaWidgets.xml
%exclude %{python3_sitearch}/pyanaconda/rescue.py*
%exclude %{python3_sitearch}/pyanaconda/__pycache__/rescue.*
%exclude %{python3_sitearch}/pyanaconda/ui/gui/*
%exclude %{python3_sitearch}/pyanaconda/ui/tui/*
%ifarch %livearches
%{_sbindir}/liveinst 
%{_bindir}/liveinst
%{_libexecdir}/liveinst-setup.sh
%{_datadir}/applications/*.desktop
%{_sysconfdir}/xdg/autostart/*.desktop
%config(noreplace) %{_sysconfdir}/pam.d/*
%config(noreplace) %{_sysconfdir}/security/console.apps/* 
%endif

%files        tui
%{python3_sitearch}/pyanaconda/rescue.py
%{python3_sitearch}/pyanaconda/__pycache__/rescue.*
%{python3_sitearch}/pyanaconda/ui/tui/*

%files        devel
%{_libdir}/libAnacondaWidgets.so
%{_includedir}/*
%{_datadir}/glade/catalogs/AnacondaWidgets.xml
%{_datadir}/gtk-doc

%changelog
* Wed Jan 15 2020 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-21
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add boot options for kdump.

* Sat Jan 11 2020 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-20
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add boot options for raid 3408

* Wed Jan 8 2020 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-19
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:modify arguments parsing

* Wed Jan 1 2020 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-18
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:bugfix for encrypting partition

* Mon Dec 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-17
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:bugfix in setup

* Mon Dec 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-16
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:bugfix in network spokes when add virtual devices


* Mon Dec 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-15
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix bug

* Mon Dec 23 2019 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-14
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:modify the patches

* Mon Dec 16 2019 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-13
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:modify interface is extended in Chinese mode

* Thu Dec 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-12
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add quiet cmdline args for x86

* Tue Oct 22 2019 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-11
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add dracut-live packages as requires 

* Mon Oct 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-10
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add anaconda-core and anaconda-tui package

* Sun Oct 13 2019 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-9
- Package init
