%define _empty_manifest_terminate_build 0
Name:    anaconda
Version: 33.19
Release: 12
Summary: Graphical system installer
License: GPLv2+ and MIT
URL:     http://fedoraproject.org/wiki/Anaconda
Source0: https://github.com/rhinstaller/anaconda/archive/%{name}-%{version}.tar.bz2
Source1: openeuler.conf

Patch6000:    Fix-hiding-of-network-device-activation-switch.patch

Patch9000:    add-passwd-policy.patch
Patch9001:    fix-hostname-info.patch
Patch9002:    disable-set-passwd-without-confirmation.patch
Patch9003:    bugfix-logo-display-in-low-screen-resolution.patch
Patch9004:    make-name-not-force-to-uppercase.patch
Patch9005:    bugfix-GUI-nfs-unknown-error.patch
Patch9006:    hide-help-button.patch
Patch9007:    modify-interface-is-extended-in-Chinese-mode.patch
Patch9008:    remove-vender-issue-in-netdev.patch
Patch9009:    modify-arguments-parsing.patch
Patch9011:    disable-product-name-in-welcome-is-uppercase.patch
Patch9012:    modify-default-timezone.patch
Patch9013:    modify-network-hostname-dot-illegal.patch
Patch9014:    disable-ssh-login-checkbox.patch
Patch9015:    bugfix-add-kdump-parameter-into-kernel-cmdline.patch
Patch9016:    bugfix-fix-password-policy.patch
Patch9017:    add-boot-args-for-smmu-and-video.patch
Patch9018:    disable-disk-encryption.patch

Patch6001:    anaconda-Fix-stage2-as-default-sources.patch
Patch6002:    anaconda-Allow-to-detect-devices-with-the-iso9660-file-system.patch
Patch6003:    bugfix-do-not-test-if-repo-is-valid-based-on-treeinfo-file.patch
Patch6004:    bugfix-move-verify-valid-installtree-to-source-module-utils.patch
Patch6005:    bugfix-add-tests-for-verify-valid-installtree-function.patch
Patch6006:    bugfix-rename-function-for-a-simple-check-for-DNF-repository.patch

Patch9023:    bugfix-add-dnf-transaction-timeout.patch

Patch6007:    fix-0-storage-devices-selected.patch
Patch6008:    fix-remove-unknow-partition-is-sda-failed.patch

%define dbusver 1.2.3
%define dnfver 3.6.0
%define dracutver 034-7
%define fcoeutilsver 1.0.12-3.20100323git
%define gettextver 0.19.8
%define gtk3ver 3.22.17
%define helpver 22.1-1
%define isomd5sum 1.0.10
%define langtablever 0.0.49
%define libarchivever 3.0.4
%define libblockdevver 2.1
%define libtimezonemapver 0.4.1-2
%define libxklavierver 5.4
%define mehver 0.23-1
%define nmver 1.0
%define pykickstartver 3.25-1
%define pypartedver 2.5-2
%define rpmver 4.10.0
%define simplelinever 1.1-1
%define utillinuxver 2.15.1
%define dasbusver 0.4
BuildRequires: python3-pygments

BuildRequires: audit-libs-devel libtool gettext-devel >= %{gettextver} gtk3-devel >= %{gtk3ver}
BuildRequires: gtk-doc gtk3-devel-docs >= %{gtk3ver} glib2-doc gobject-introspection-devel
BuildRequires: glade-devel libgnomekbd-devel libxklavier-devel >= %{libxklavierver} pango-devel
BuildRequires: python3-kickstart >= %{pykickstartver} python3-devel python3-nose systemd
BuildRequires: rpm-devel >= %{rpmver} libarchive-devel >= %{libarchivever} gdk-pixbuf2-devel
BuildRequires: libtimezonemap-devel >= %{libtimezonemapver} libxml2
BuildRequires: gsettings-desktop-schemas metacity

Requires: anaconda-core = %{version}-%{release}
Requires: anaconda-tui = %{version}-%{release}
Requires: libblockdev-plugins-all >= %{libblockdevver} realmd isomd5sum >= %{isomd5sum}
Requires: kexec-tools createrepo_c tmux gdb rsync python3-meh-gui >= %{mehver}
Requires: adwaita-icon-theme python3-kickstart
Requires: tigervnc-server-minimal libxklavier >= %{libxklavierver} libgnomekbd
Requires: libtimezonemap >= %{libtimezonemapver} xz
Requires: nm-connection-editor keybinder3 anaconda-user-help >= %{helpver} yelp system-logos
Requires: python3 dracut >= %{dracutver} dracut-network dracut-live
%ifarch %{ix86} x86_64
BuildRequires: desktop-file-utils
Requires: zenity fcoe-utils >= %{fcoeutilsver}
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
The anaconda package is a metapackage for the Anaconda installer.

%package core
Summary: Core of the Anaconda installer
Requires: python3-libs python3-dnf >= %{dnfver} python3-blivet >= 1:3.2.2-1
Requires: python3-blockdev >= %{libblockdevver} rpm-python3 >= %{rpmver} python3-productmd
Requires: libreport-anaconda >= 2.0.21-1 libselinux-python3 python3-meh >= %{mehver}
Requires: python3-pyparted >= %{pypartedver} python3-requests python3-requests-file
Requires: python3-requests-ftp python3-kickstart >= %{pykickstartver}
Requires: python3-langtable >= %{langtablever} util-linux >= %{utillinuxver} python3-gobject-base
Requires: python3-dbus python3-pwquality python3-systemd python3-dasbus >= %{dasbusver}
Requires: cracklib-dicts python3-pytz teamd NetworkManager >= %{nmver} NetworkManager-libnm >= %{nmver}
Requires: NetworkManager-team dhclient kbd chrony python3-ntplib systemd python3-pid
Requires: python3-ordered-set >= 2.0.0 glibc-langpack-en dbus-daemon
Requires: flatpak-libs
# required because of the rescue mode and VNC question
Requires: anaconda-tui = %{version}-%{release}
Provides: anaconda-images = %{version}-%{release}
Obsoletes: anaconda-images <= 10
Provides: anaconda-runtime = %{version}-%{release}
Obsoletes: anaconda-runtime < %{version}-%{release}
Obsoletes: booty <= 0.107-1

# Ensure it's not possible for a version of grubby to be installed
# that doesn't work with btrfs subvolumes correctly...
Conflicts: grubby < 8.40-10

%ifarch %{ix86} x86_64
Requires: usermode
%endif

%description core
The anaconda-core package contains the program which was used to install your
system.

%package tui
Summary: Textual user interface for the Anaconda installer
Requires: anaconda-core = %{version}-%{release} python3-simpleline >= %{simplelinever}

%description tui
This package contains textual user interface for the Anaconda installer.


%package devel
Summary: Development files for anaconda-widgets
Requires: glade
Requires: %{name}-widgets = %{version}-%{release}

%description devel
This package contains libraries and header files needed for writing the anaconda
installer.  It also contains Python and Glade support files, as well as
documentation for working with this library.


%prep
%autosetup -n %{name}-%{version} -p1

%build
# use actual build-time release number, not tarball creation time release number
%configure ANACONDA_RELEASE=%{release}
%make_build

%install
%make_install
%delete_la

# install openEuler conf for anaconda
install -m 0755 %{SOURCE1} %{buildroot}/%{_sysconfdir}/%{name}/product.d/

# Create an empty directory for addons
install -d -m 0755 %{buildroot}%{_datadir}/anaconda/addons

%ifarch %{ix86} x86_64
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/liveinst.desktop
%endif

# If no langs found, keep going
%find_lang %{name} || :

%ldconfig_scriptlets

%ifarch %{ix86} x86_64
%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
%endif

%files
%defattr(-,root,root)
%license COPYING
%{_libdir}/libAnacondaWidgets.so.*
%{_libdir}/girepository*/AnacondaWidgets*typelib
%{python3_sitearch}/gi/overrides/*
%{python3_sitearch}/pyanaconda/ui/gui/*
%{_prefix}/libexec/anaconda/dd_*
%{_prefix}/lib/dracut/modules.d/80%{name}/*
%exclude %{python3_sitearch}/pyanaconda/ui/gui/spokes/blivet_gui.*

%files core
%defattr(-,root,root)
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
%exclude %{_datadir}/anaconda/ui/spokes/blivet_gui.*
%exclude %{_datadir}/glade/catalogs/AnacondaWidgets.xml
%exclude %{python3_sitearch}/pyanaconda/rescue.py*
%exclude %{python3_sitearch}/pyanaconda/__pycache__/rescue.*
%exclude %{python3_sitearch}/pyanaconda/ui/gui/*
%exclude %{python3_sitearch}/pyanaconda/ui/tui/*
%{_bindir}/analog
%{_bindir}/anaconda-cleanup
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*
%dir %{_sysconfdir}/%{name}/conf.d
%config %{_sysconfdir}/%{name}/conf.d/*
%dir %{_sysconfdir}/%{name}/product.d
%config %{_sysconfdir}/%{name}/product.d/*
%{_sbindir}/liveinst 
%{_bindir}/liveinst
%{_libexecdir}/liveinst-setup.sh
%{_datadir}/applications/*.desktop
%{_sysconfdir}/xdg/autostart/*.desktop
%config(noreplace) %{_sysconfdir}/pam.d/*
%config(noreplace) %{_sysconfdir}/security/console.apps/* 

%files tui
%{python3_sitearch}/pyanaconda/rescue.py
%{python3_sitearch}/pyanaconda/__pycache__/rescue.*
%{python3_sitearch}/pyanaconda/ui/tui/*

%files devel
%{_libdir}/libAnacondaWidgets.so
%{_libdir}/glade/modules/libAnacondaWidgets.so
%{_includedir}/*
%{_datadir}/glade/catalogs/AnacondaWidgets.xml
%{_datadir}/gtk-doc

%changelog
* Mon Oct 26 2020 fengtao <fengtao40@huawei.com> - 33.19-12
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:bugfix for partitioning when sda exists a ext4 filesystem

* Sat Sep 26 2020 fengtao <fengtao40@huawei.com> - 33.19-11
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add dnf transactions timeout

* Thu Sep 17 2020 zhuqingfu <zhuqingfu1@huawei.com> - 33.19-10
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:do not require treeinfo

* Wed Sep 16 2020 xiaqirong <xiaqirong1@huawei.com> - 33.19-9
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:disable disk encryption

* Fri Sep 11 2020 fengtao <fengtao40@huawei.com> - 33.19-8
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add boot args for smmu and video

* Thu Sep 10 2020 zhangqiumiao <zhangqiumiao1@huawei.com> - 33.19-7
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:revert add-passwd-check-policy.patch and bugfix-fix-encrypt-weak-passphrase-save.patch
       fix password policy

* Fri Sep 4 2020 zhangqiumiao <zhangqiumiao1@huawei.com> - 33.19-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix password policy

* Mon Aug 31 2020 zhangqiumiao <zhangqiumiao1@huawei.com> - 33.19-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix kdump patch err

* Fri Aug 28 2020 zhangqiumiao <zhangqiumiao1@huawei.com> - 33.19-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:remove dependency on blivet-gui-runtime

* Fri Aug 7 2020 fengtao <fengtao40@huawei.com> - 33.19-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix stage2 as default sources

* Tue Jul 14 2020 zhangqiumiao <zhangqiumiao1@huawei.com> - 33.19-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add kdump parameter into kernel cmdline

* Fri Jun 19 2020 fengtao <fengtao40@huawei.com> - 33.19-1
- update version to 33.19

* Mon Mar 9 2020 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-28
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add boot options for dummy

* Wed Feb 12 2020 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-27
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Remove initThreading method from pyanaconda.threading

* Thu Feb 06 2020 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-26
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:modify network hostname dot error

* Thu Jan 16 2020 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-25
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:modify default timezone and zh_CN.po

* Thu Jan 16 2020 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-24
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix setup fail in decode

* Thu Jan 16 2020 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-23
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:modify openeuler in welcome to lowercase

* Thu Jan 16 2020 openEuler Buildteam <buildteam@openeuler.org> - 29.24.7-22
- optimization the patch

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
