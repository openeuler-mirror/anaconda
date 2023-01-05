%define _empty_manifest_terminate_build 0
Name:    anaconda
Version: 33.19
Release: 52
Summary: Graphical system installer
License: GPLv2+ and MIT
URL:     http://fedoraproject.org/wiki/Anaconda
Source0: https://github.com/rhinstaller/anaconda/archive/%{name}-%{version}.tar.bz2
Source1: openeuler.conf
Source2: euleros.conf
Source3: hce.conf

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
Patch9016:    bugfix-fix-password-policy.patch
%if ! 0%{?openEuler}
Patch9018:    disable-disk-encryption.patch
%endif
Patch9019:    bugfix-set-up-LD_PRELOAD-for-the-Storage-and-Services-module.patch
Patch9020:    bugfix-Propagate-a-lazy-proxy-of-the-storage-model.patch

Patch6001:    anaconda-Fix-stage2-as-default-sources.patch
Patch6002:    anaconda-Allow-to-detect-devices-with-the-iso9660-file-system.patch
Patch6003:    bugfix-do-not-test-if-repo-is-valid-based-on-treeinfo-file.patch
Patch6004:    bugfix-move-verify-valid-installtree-to-source-module-utils.patch
Patch6005:    bugfix-add-tests-for-verify-valid-installtree-function.patch
Patch6006:    bugfix-rename-function-for-a-simple-check-for-DNF-repository.patch

Patch9023:    bugfix-add-dnf-transaction-timeout.patch

Patch6007:    fix-0-storage-devices-selected.patch
Patch6008:    fix-remove-unknow-partition-is-sda-failed.patch
Patch6009:    use-modinfo-to-check-ko-before-modprobe.patch
Patch6010:    ntp-servers-improve-001-Create-a-new-DBus-structure-for-time-sources.patch
Patch6011:    ntp-servers-improve-002-Use-the-structure-for-time-sources-in-ntp-py.patch
Patch6012:    ntp-servers-improve-003-Use-the-structure-for-time-sources-in-the-Timezone-module.patch
Patch6013:    ntp-servers-improve-004-Use-the-structure-for-time-sources-in-anaconda-py.patch
Patch6014:    ntp-servers-improve-005-Use-the-structure-for-time-sources-in-network-py.patch
Patch6015:    ntp-servers-improve-006-Add-support-for-the-NTP-server-status-cache.patch
Patch6016:    ntp-servers-improve-007-Add-support-for-generating-a-summary-of-the-NTP-servers.patch
Patch6017:    ntp-servers-improve-008-Use-the-structure-for-time-sources-in-TUI.patch
Patch6018:    ntp-servers-improve-009-Use-the-structure-for-time-sources-in-GUI.patch
Patch6019:    ntp-servers-improve-010-Add-support-for-the-timesource-kickstart-command.patch

Patch9024:    Change-length-limit-of-hostname-from-255-to-64.patch
Patch9025:    Change-topbar-background-size.patch

Patch6020:    bugfix-Schedule-timed-actions-with-the-right-selector-18516.patch
Patch6021:    bugfix-Reset-the-state-of-the-custom-partitioning-spoke.patch
Patch6022:    bugfix-Fix-regression-reading-kernel-list-when-collecting-c.patch
Patch6023:    bugfix-Fix-more-SElinux-contexts.patch
Patch6024:    bugfix-Fix-issue-when-NFS-path-is-pointing-directly-to-ISO-.patch
Patch6025:    bugfix-Create-the-initial-storage-model-during-the-initiali.patch
Patch6026:    bugfix-Always-specify-the-boot-disk.patch
Patch6027:    bugfix-Fix-passing-of-arguments-when-creating-dracut-argume.patch
Patch6028:    bugfix-Reconfigure-DNF-payload-after-options-are-set.patch
Patch6029:    bugfix-Only-pass-one-initrd-image-to-kexec.patch
Patch6030:    bugfix-Fix-creating-cached-LVs-on-encrypted-PVs.patch
Patch6031:    bugfix-Run-actions-of-the-Resize-dialog-in-the-reversed-ord.patch
Patch6032:    bugfix-Reload-treeinfo-repositories-on-every-payload-reset.patch
Patch6033:    bugfix-Remove-treeinfo-repositories-instead-of-disabling.patch
Patch6034:    bugfix-Fix-crash-on-first-entering-of-source-spoke.patch
Patch6035:    bugfix-Keep-treeinfo-repositories-disabled-after-payload-re.patch
Patch6036:    bugfix-Fix-issue-that-treeinfo-repositories-were-never-disa.patch
Patch6037:    bugfix-Fix-kickstart-file-error-with-user-groups.patch
Patch6038:    bugfix-Create-ssh-user-using-only-existing-fields-1860058.patch
Patch6039:    bugfix-Automatically-break-lines-in-labels-in-software-sele.patch
Patch6040:    bugfix-Reset-the-RAID-level-of-the-device-request-1828092.patch
Patch6041:    bugfix-Change-keyboard-ordering-to-US-layout-first-native-s.patch
Patch6042:    bugfix-Handle-exceptions-from-threads-without-new-instances.patch
Patch6043:    bugfix-network-fix-configuration-of-virtual-devices-by-boot.patch
Patch6044:    bugfix-network-do-not-try-to-activate-connection-that-has-n.patch
Patch6045:    bugfix-network-add-timeout-for-synchronous-activation-of-a-.patch
Patch6046:    bugfix-Fix-traceback-when-removing-additional-repository.patch
Patch6047:    bugfix-network-do-not-crash-when-updating-a-connection-with.patch
Patch6048:    bugfix-Do-not-mount-as-RW-in-Dracut.patch
Patch6049:    bugfix-The-underline-character-should-not-be-displayed.patch
Patch6050:    bugfix-Recognize-systemd.unit-anaconda.target-in-anaconda-g.patch
Patch6051:    bugfix-Always-clear-treeinfo-metadata-1872056.patch
Patch6052:    bugfix-Apply-onboot-policy-even-when-network-was-configured.patch
Patch6053:    bugfix-network-fix-parsing-of-hostname-from-ip-if-mac-is-de.patch
Patch6054:    bugfix-Don-t-generate-container-data-for-non-container-devi.patch
Patch6055:    bugfix-Differentiate-between-RAID-levels-of-a-device-and-it.patch
Patch6056:    bugfix-Show-warning-message-when-entered-size-is-not-valid.patch
Patch6057:    bugfix-Add-the-DBus-method-IsDeviceShrinkable-1875677.patch
Patch6058:    bugfix-Check-if-original-partitions-are-mounted-too.patch
Patch6059:    bugfix-network-get-hwadddr-when-binding-to-mac-more-robustl.patch
Patch6060:    bugfix-Fix-the-combo-box-for-an-URL-type-of-additional-repo.patch
Patch6061:    bugfix-Never-mount-partitions-on-a-disk-with-the-iso9660-fi.patch
Patch6062:    bugfix-Add-missing-make-BuildRequires.patch
Patch6063:    bugfix-Allow-to-format-selected-DASDs.patch
Patch6064:    bugfix-Add-selinux-0-boot-parameter-when-SELinux-is-set-to-.patch
Patch6065:    bugfix-Root-password-is-mandatory-if-there-is-not-admin-use.patch
Patch6066:    bugfix-Fix-traceback-when-starting-installation-with-inst.c.patch
Patch6067:    bugfix-Fix-checking-ssl-certificate-for-metadata-1745064.patch
Patch6068:    bugfix-Fix-error-in-initrd-shift-count-out-of-range.patch
Patch6069:    bugfix-Fix-the-logic-for-enabling-latest-updates.patch
Patch6070:    bugfix-Don-t-enter-spokes-after-we-leave-the-Summary-hub.patch
Patch6071:    bugfix-do-not-mount-dbus-source.patch
Patch6072:    fix-xorg-timeout-and-throw-exception.patch
Patch6073:    bugfix-Fix-issue-when-ns_info-cannot-be-retrieved-for-NVDim.patch
Patch6074:    bugfix-Fix-SECTION-headers-in-docstrings.patch
Patch6075:    change-inst-repo-default-value.patch
Patch6076:    delete-datezone-map.patch

Patch6077:    backport-fix-boot-options-generated-by-dracut-module.patch
Patch9027:    bugfix-remove-flatpack-support.patch
Patch9028:    Change-sidebar-background-size.patch
Patch6078:    bugfix-Cancel-planned-manual-update-of-system-time-on-turni.patch
Patch9029:    support-use-sm3-crypt-user-password.patch
Patch6079:    backport-remove-authconfig-support.patch
Patch6080:    backport-change-the-grub2-user-cfg-permission-from-0700-to-0600.patch
Patch6081:    bugfix-change-the-startup-mode-of-do_transaction-sub-proces.patch
Patch6082:    Support-configuration-of-additional-boot-arguments.patch

Patch6083:    backport-revert-Set-default-entry-to-the-BLS-id-instead-of-th.patch
Patch9030:    bugfix-Solve-the-problem-that-the-circular-loading-progress-bar-does-not-rotate.patch
%ifarch sw_64
Patch6085:    anaconda-33.19.sw.patch
%endif
%ifarch loongarch64
Patch6086:    0001-add-loongarch-support-for-anaconda-33.19.patch
Patch6087:    0001-add-BOOTLOONGARCH.EFI-for-anaconda.patch
%endif

Patch6088:    backport-Round-the-required-device-size-up.patch
Patch6089:    backport-Run-restorecon-in-chroot-when-handling-home-dirs.patch
Patch6090:    backport-dracut-handle-compressed-kernel-modules.patch
Patch6091:    backport-network-use-separate-main-conext-for-NM-client-in-threads.patch

Patch9031:    bugfix-translate-the-prompt-information-of-hostname-.patch
Patch9032:    bugfix-translate-the-tips-about-expected-capacity-into-Chin.patch

%define dbusver 1.2.3
%define dnfver 3.6.0
%define dracutver 034-7
%define gettextver 0.19.8
%define gtk3ver 3.22.17
%define isomd5sum 1.0.10
%define langtablever 0.0.49
%define libarchivever 3.0.4
%define libblockdevver 2.1
%define libxklavierver 5.4
%define mehver 0.23-1
%define nmver 1.0
%define pykickstartver 3.27-1
%define pypartedver 2.5-2
%define rpmver 4.10.0
%define simplelinever 1.1-1
%define utillinuxver 2.15.1
%define dasbusver 0.4
BuildRequires: python3-pygments

BuildRequires: audit-libs-devel libtool gettext-devel >= %{gettextver} gtk3-devel >= %{gtk3ver}
BuildRequires: gtk-doc gtk3-devel-docs >= %{gtk3ver} glib2-doc gobject-introspection-devel
BuildRequires: glade-devel libgnomekbd-devel libxklavier-devel >= %{libxklavierver} pango-devel
BuildRequires: python3-kickstart >= %{pykickstartver} python3-devel systemd
BuildRequires: rpm-devel >= %{rpmver} libarchive-devel >= %{libarchivever} gdk-pixbuf2-devel
BuildRequires: libxml2
BuildRequires: gsettings-desktop-schemas metacity

Requires: anaconda-core = %{version}-%{release}
Requires: anaconda-tui = %{version}-%{release}
Requires: libblockdev-plugins-all >= %{libblockdevver} realmd isomd5sum >= %{isomd5sum}
Requires: kexec-tools createrepo_c tmux gdb rsync python3-meh-gui >= %{mehver}
Requires: adwaita-icon-theme python3-kickstart
Requires: tigervnc-server-minimal libxklavier >= %{libxklavierver} libgnomekbd
Requires: nm-connection-editor keybinder3 system-logos
Requires: python3
%ifarch %{ix86} x86_64
BuildRequires: desktop-file-utils
Requires: zenity
%endif

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
Conflicts: anaconda < %{version}-41
 
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
install -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/%{name}/product.d/
install -m 0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}/product.d/
install -m 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/%{name}/product.d/


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

%files dracut
%dir %{_prefix}/lib/dracut/modules.d/80%{name}
%{_prefix}/lib/dracut/modules.d/80%{name}/*
%{_prefix}/libexec/anaconda/dd_*

%changelog
* Tue Jan 03 2023 sunhai <sunhai10@huawei.com> - 33.19-52
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:sync patches

* Thu Nov 10 2022 Wenlong Zhang <zhangwenlong@loongson.cn> - 33.19-51
- ID:NA
- SUG:NA
- DESC: Increase firmware compatibility for loongarch

* Sun Nov 13 2022 sunhai <sunhai10@huawei.com> - 33.19-50
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:round the required device size up
       run restorecon in chroot when handling home dirs

* Mon Mar 28 2022 Wenlong Zhang <zhangwenlong@loongson.cn> - 33.19-49
- ID:NA
- SUG:NA
- DESC: add loongarch support for anaconda

* Tue Oct 18 2022 wuzx<wuzx1226@qq.com> - 33.19-48
- Type:feature
- CVE:NA
- SUG:NA
- DESC:Add sw64 architecture

* Thu Sep 1 2022 sunhai <sunhai10@huawei.com> - 33.19-47
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:solve the problem that the circular loading progress bar does not rotate

* Tue Aug 24 2022 zhangqiumiao <zhangqiumiao1@huawei.com> - 33.19-46
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix missing group information in dnf

* Mon Aug 8 2022 wanglu <wanglu210@huawei.com> - 33.19-45
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

* Wed Jan 26 2022 songnannan <songnannan2@huawei.com> - 33.19-37
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:support sm3

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
