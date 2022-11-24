%define _empty_manifest_terminate_build 0
Name:    anaconda
Version: 36.16.5
Release: 6
Summary: Graphical system installer
License: GPLv2+ and MIT
URL:     http://fedoraproject.org/wiki/Anaconda
Source0: https://github.com/rhinstaller/%{name}/releases/download/%{name}-%{version}-1/%{name}-%{version}.tar.bz2
Source1: openeuler.conf
Source2: euleros.conf
Source3: hce.conf
Source4: disable-disk-encryption.patch

Patch9000:    add-passwd-policy.patch
Patch9001:    bugfix-GUI-nfs-unknown-error.patch
Patch9002:    bugfix-set-up-LD_PRELOAD-for-the-Storage-and-Services-module.patch
Patch9003:    bugfix-Solve-the-problem-that-the-circular-loading-progress-bar-does-not-rotate.patch
Patch9004:    change-inst-repo-default-value.patch
%if ! 0%{?openEuler}
Patch9005:    disable-disk-encryption.patch
%endif
Patch9006:    disable-ssh-login-checkbox.patch
Patch9007:    fix-hostname-info.patch
Patch9008:    hide-help-button.patch
Patch9009:    modify-interface-is-extended-in-Chinese-mode.patch
Patch9010:    modify-timezone-and-delete-datezone-map.patch
Patch9011:    remove-vender-issue-in-netdev.patch
Patch9012:    Support-configuration-of-additional-boot-arguments.patch
Patch9013:    support-use-sm3-crypt-user-password.patch
Patch9014:    bugfix-with-use-local-kickstart-version.patch
Patch9015:    bugfix-change-gnome-kiosk-to-use-metacity.patch
Patch9016:    bugfix-add-log-and-background.patch

%define dasbusver 1.3
%define dbusver 1.2.3
%define dnfver 3.6.0
%define dracutver 034-7
%define gettextver 0.19.8
%define gtk3ver 3.22.17
%define isomd5sumver 1.0.10
%define langtablever 0.0.54
%define libarchivever 3.0.4
%define libblockdevver 2.1
%define libxklavierver 5.4
%define mehver 0.23-1
%define nmver 1.0
%define pykickstartver 3.32-1
%define pypartedver 2.5-2
%define pythonblivetver 1:3.4.0-1
%define rpmver 4.15.0
%define simplelinever 1.1-1
%define utillinuxver 2.15.1
BuildRequires: python3-pygments

BuildRequires: audit-libs-devel libtool gettext-devel >= %{gettextver} gtk3-devel >= %{gtk3ver}
BuildRequires: gtk-doc gtk3-devel-docs >= %{gtk3ver} glib2-doc gobject-introspection-devel
BuildRequires: glade-devel libgnomekbd-devel libxklavier-devel >= %{libxklavierver} pango-devel
BuildRequires: make
BuildRequires: python3-kickstart >= %{pykickstartver} python3-devel systemd
BuildRequires: rpm-devel >= %{rpmver} libarchive-devel >= %{libarchivever} gdk-pixbuf2-devel
BuildRequires: libxml2
BuildRequires: gsettings-desktop-schemas metacity

Requires: anaconda-core = %{version}-%{release}
Requires: anaconda-tui = %{version}-%{release}
Requires: libblockdev-plugins-all >= %{libblockdevver} realmd isomd5sum >= %{isomd5sumver}
Requires: kexec-tools createrepo_c tmux gdb rsync python3-meh-gui >= %{mehver}
Requires: adwaita-icon-theme python3-kickstart
Requires: tigervnc-server-minimal libxklavier >= %{libxklavierver} libgnomekbd
Requires: nm-connection-editor keybinder3 system-logos
Requires: python3
BuildRequires: desktop-file-utils
Requires: zenity

Provides:       anaconda-gui = %{version}-%{release}
Obsoletes:      anaconda-gui < %{version}-%{release}

Provides:       anaconda-widgets = %{version}-%{release}
Obsoletes:      anaconda-widgets < %{version}-%{release}

Provides:       anaconda-install-env-deps = %{version}-%{release} 
Obsoletes:      anaconda-install-env-deps < %{version}-%{release}

%description
The anaconda package is a metapackage for the Anaconda installer.

%package core
Summary: Core of the Anaconda installer
Requires: python3-libs python3-dnf >= %{dnfver} python3-blivet >= %{pythonblivetver}
Requires: python3-blockdev >= %{libblockdevver} rpm-python3 >= %{rpmver} python3-productmd
Requires: libreport-anaconda >= 2.0.21-1 libselinux-python3 python3-meh >= %{mehver}
Requires: python3-pyparted >= %{pypartedver} python3-requests python3-requests-file
Requires: python3-requests-ftp python3-kickstart >= %{pykickstartver}
Requires: python3-langtable >= %{langtablever} util-linux >= %{utillinuxver} python3-gobject-base
Requires: python3-dbus python3-pwquality python3-systemd python3-dasbus >= %{dasbusver}
Requires: python3-packaging
Requires: cracklib-dicts python3-pytz teamd NetworkManager >= %{nmver} NetworkManager-libnm >= %{nmver}
Requires: NetworkManager-team kbd chrony systemd python3-pid
Requires: python3-ordered-set >= 2.0.0 glibc-langpack-en dbus-daemon
Requires: systemd-resolved
# Required by the systemd service anaconda-fips.
Requires: crypto-policies
Requires: /usr/bin/update-crypto-policies
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
Requires: usermode

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

%package dracut
Summary: The anaconda dracut module
Requires: dracut >= %{dracutver}
Requires: dracut-network
Requires: dracut-live
Requires: xz
Requires: python3-kickstart
 
%description dracut
The 'anaconda' dracut module handles installer-specific boot tasks and
options. This includes driver disks, kickstarts, and finding the anaconda
runtime on NFS/HTTP/FTP servers or local disks.

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
%ifarch x86_64
sed -i "/^additional_arguments =*/ s/$/ crashkernel=512M/" %{SOURCE1}
sed -i "/^additional_arguments =*/ s/$/ panic=3 nmi_watchdog=1/" %{SOURCE2}
sed -i "/^additional_arguments =*/ s/$/ panic=3 nmi_watchdog=1/" %{SOURCE3}
%endif

%ifarch aarch64
sed -i "/^additional_arguments =*/ s/$/ crashkernel=1024M,high smmu.bypassdev=0x1000:0x17 smmu.bypassdev=0x1000:0x15/" %{SOURCE1}
sed -i "/^additional_arguments =*/ s/$/ panic=1 vga=0x317 nohz=off smmu.bypassdev=0x1000:0x17 smmu.bypassdev=0x1000:0x15/" %{SOURCE2}
sed -i "/^additional_arguments =*/ s/$/ panic=1 vga=0x317 nohz=off smmu.bypassdev=0x1000:0x17 smmu.bypassdev=0x1000:0x15/" %{SOURCE3}
%endif
install -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/%{name}/profile.d/
install -m 0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}/profile.d/
install -m 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/%{name}/profile.d/


# Create an empty directory for addons
install -d -m 0755 %{buildroot}%{_datadir}/anaconda/addons

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/liveinst.desktop

# If no langs found, keep going
%find_lang %{name} || :

%ldconfig_scriptlets

%ifarch %{ix86} x86_64
%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
%endif

#Anaconda test cases require python3-nose. However, python3-nose on 22.03 has been deleted due to aging. 
#As a result, the anaconda lacks dependency. Now, the anaconda needs to remove the python3-nose dependency. 
#However, the removal will affect the test cases.

%files
%defattr(-,root,root)
%license COPYING
%{_libdir}/libAnacondaWidgets.so.*
%{_libdir}/girepository*/AnacondaWidgets*typelib
%{python3_sitearch}/gi/overrides/*
%{python3_sitearch}/pyanaconda/ui/gui/*
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
%dir %{_sysconfdir}/%{name}/profile.d
%config %{_sysconfdir}/%{name}/profile.d/*
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

%files dracut
%dir %{_prefix}/lib/dracut/modules.d/80%{name}
%{_prefix}/lib/dracut/modules.d/80%{name}/*
%{_prefix}/libexec/anaconda/dd_*

%changelog
* Thu Nov 24 2022 sunhai <sunhai10@huawei.com> - 36.16.5-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add logo with install
       the kickstart version change to patch

* Wed Nov 23 2022 sunhai <sunhai10@huawei.com> - 36.16.5-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:pxe kickstart version with local pykickstart
       and with build save patch by source4

* Mon Nov 21 2022 sunhai <sunhai10@huawei.com> - 36.16.5-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:open disk encryption on openEuler

* Tue Nov 15 2022 sunhai <sunhai10@huawei.com> - 36.16.5-3
- ID:NA
- SUG:NA
- DESC: fix install with tui and gui

* Fri Nov 11 2022 sunhai <sunhai10@huawei.com> - 36.16.5-2
- ID:NA
- SUG:NA
- DESC: use kickstart version with local pykickstart 

* Tue Nov 08 2022 sunhai <sunhai10@huawei.com> - 36.16.5-1
- ID:NA
- SUG:NA
- DESC:update anaconda to 36.16.5

* Mon Mar 28 2022 Wenlong Zhang <zhangwenlong@loongson.cn> - 33.19-49
- ID:NA
- SUG:NA
- DESC: add loongarch support for anaconda

* Tue Oct 18 2022 wuzx<wuzx1226@qq.com> - 33.19-48
- Type:feature
- CVE:NA
- SUG:NA
- DESC:Add sw64 architecture

* Wed Sep 21 2022 sunhai <sunhai10@huawei.com> - 33.19-47
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:solve the problem that the circular loading progress bar does not rotate

* Tue Aug 23 2022 zhangqiumiao <zhangqiumiao1@huawei.com> - 33.19-46
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix missing group information in dnf

* Fri Aug 5 2022 wanglu <wanglu210@huawei.com> - 33.19-45
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix a mistake about revert "Set default entry to the BLS id instead of the entry index"

* Thu Aug 4 2022 wanglu <wanglu210@huawei.com> - 33.19-44
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:revert "Set default entry to the BLS id instead of the entry index"

* Fri Apr 8 2022 zhangqiumiao <zhangqiumiao1@huawei.com> - 33.19-43
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:change the grub2 user.cfg permission from 0700 to 0600

* Thu Apr 7 2022 zhangqiumiao <zhangqiumiao1@huawei.com> - 33.19-42
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add support for configuration of additional boot arguments
       change the startup mode of do_transaction sub process to spawn

* Sat Mar 05 2022 gaihuiying <eaglegai@163.com> - 33.19-41
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:separate anaconda-dracut

* Mon Feb 21 2022 gaihuiying <eaglegai@163.com> - 33.19-40
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:remove yelp and foce-utils from requires

* Sun Jan 30 2022 yanan <yanan@huawei.com> - 33.19-39
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:remove authconfig support

* Thu Jan 27 2022 liufushou <liufushou@live.cn> - 33.19-38
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:let networking up after reboot

* Wed Jan 26 2022 zhujunhao <zhujunhao11@huawei.com> - 33.19-37
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:support use sm3 crypt user password

* Sun Jan 23 2022 liuxin <liuxin350@huawei.com> - 33.19-36
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Cancel planned manual update of system time on turning ntp on

* Sat Jan 22 2022 fengtao <fengtao40@huawei.com> - 33.19-35
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:revert "fix deadlock when forking in multithread"

* Thu Jan 13 2022 gaihuiying <gaihuiying1@huawei.com> - 33.19-34
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:remove flatpak support in source code

* Tue Jan 11 2022 gaihuiying <gaihuiying1@huawei.com> - 33.19-33
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:remove anaconda-user-help dependency

* Fri Dec 31 2021 xihaochen <xihaochen@huawei.com> - 33.19-32
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:remove flatpak dependency

* Fri Dec 31 2021 xihaochen <xihaochen@huawei.com> - 33.19-31
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:remove python3-nose dependency

* Fri Oct 29 2021 zhujunhao <zhujunhao8@huawei.com> - 33.19-30
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix boot options generated by dracut module

* Sat Aug 28 2021 yanan <yanan@huawei.com> - 33.19-29
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix deadlock when forking in multithread

* Mon Aug 23 2021 wangce <wangce@uniontech.com> - 33.19-28
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Change sidebar background size

* Sat Aug 7 2021 zhujunhao <zhujunhao8@huawei.com> - 33.19-27
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:delete date zone map

* Thu Jun 24 2021 youyifeng <ctyuncommiter05@chinatelecom.cn> - 33.19-26
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:change inst.repo default value

* Mon Jun 21 2021 gaihuiying <gaihuiying1@huawei.com> - 33.19-25
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:change topbar background size

* Mon Jun 21 2021 zhangqiumiao <zhangqiumiao1@huawei.com> - 33.19-24
- Type:requirement
- ID:NA
- SUG:NA
- DESC:replace openEuler by %{_vendor}

* Mon Jun 21 2021 liuxin <liuxin264@huawei.com> - 33.19-23
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Fix section headers in docstrings

* Wed May 19 2021 liuxin <liuxin264@huawei.com> - 33.19-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Fix issue when ns_info cannot be retrieved for NVDimm namespace

* Sat May 8 2021 fengtao <fengtao40@huawei.com> - 33.19-21
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix xorg timeout and throw exception

* Thu Apr 29 2021 zhangrui <zhangrui182@huawei.com> - 33.19-20
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:do not mount dbus sources

* Mon Mar 29 2021 xuxiaolong <xuxiaolon23@huawei.com> - 33.19-19
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:sync 50 bugfix commit from github

* Sat Mar 27 2021 zhangrui <zhangrui182@huawei.com> - 33.19-18
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:reset the state of the custom partitioning spoke

* Mon Jan 25 2021 liuxin <liuxin264@huawei.com> - 33.19-17
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Propagate a lazy proxy o the storage model

* Thu Jan 14 2021 yuboyun <yuboyun@huawei.com> - 33.19-16
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:set up LD_PRELOAD for the Storage and Services module

* Thu Dec 10 2020 zhouyihang <zhouyihang3@huawei.com> - 33.19-15
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Change length limit of hostname from 255 to 64

* Fri Dec 04 2020 gaihuiying <gaihuiying1@huawei.com> - 33.19-14
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:improve ntp servers to fix unkown error

* Sat Nov 28 2020 lunankun <lunankun@huawei.com> - 33.19-13
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix issue of iscsi_tcp and sha256 not found

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
