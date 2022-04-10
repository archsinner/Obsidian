# Linux From Scratch

## Version 11.1

## Published March 1st, 2022

### Created by Gerard Beekmans

### Managing Editor: Bruce Dubbs

Copyright © 1999-2022 Gerard Beekmans

Copyright © 1999-2022, Gerard Beekmans

All rights reserved.

This book is licensed under a [Creative Commons License](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#CC "F.1. Creative Commons License").

Computer instructions may be extracted from the book under the [MIT License](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#MIT "F.2. The MIT License").

Linux® is a registered trademark of Linus Torvalds.

---

# Table of Contents

-   Preface
    -   [[Computer Science/Operating Systems/Linux/LFS/Preface/Foreword]]
    -   [[Audience]]
    -   [[LFS Target Architectures]]
    -   [[Prerequisites]]
    -   [[LFS and Standards]]
    -   [[Rationale for Packages in the Book]]
    -   [[Typography]]
    -   [[Structure]]
    -   [[Errata and Security Advisories]]
-   I. Introduction
    -   1. Introduction
        -   [[How to Build an LFS System]]
        -   [[What's new since the last release]]
        -   [[Changelog]]
        -   [[Resources]]
        -   [[Help]]
-   II. Preparing for the Build
    -   2. Preparing the Host System
        -   [[Chapter 2 Introduction]]
        -   [[Host System Requirements]]
        -   [[Building LFS in Stages]]
        -   [[Creating a New Partition]]
        -   [[Creating a File System on the Partition]]
        -   [[Setting The $LFS Variable]]
        -   [[Mounting the New Partition]]
    -   3. Packages and Patches
        -   [[Chapter 3 Introduction]]
        -   [[All Packages]]
        -   [[Needed Patches]]
    -   4. Final Preparations
        -   [[Chapter 4 Introduction]]
        -   [[Creating a limited directory layout in LFS filesystem]]
        -   [[Adding the LFS User]]
        -   [[Setting Up the Environment]]
        -   [[About SBUs]]
        -   [[About the Test Suites]]
-   III. Building the LFS Cross Toolchain and Temporary Tools  
    -  Important Preliminary Material
        -   [[Part III Introduction]]
        -   [[Toolchain Technical Notes]]
        -   [[General Compilation Instructions]]
    -   5. Compiling a Cross-Toolchain
        -   [[Chapter 5 Introduction]]
        -   [[Binutils-2.38 - Pass 1]]
        -   [[GCC-11.2.0 - Pass 1]]
        -   [[Linux-5.16.9 API Headers]]
        -   [[Glibc-2.35]]
        -   [[Libstdc++ from GCC-11.2.0, Pass 1]]
    -   6. Cross Compiling Temporary Tools
        -   [[6.1. Chapter 6 Introduction]]
        -   [[6.2. M4-1.4.19]]
        -   [[6.3. Ncurses-6.3]]
        -   [[6.4. Bash-5.1.16]]
        -   [[6.5. Coreutils-9.0]]
        -   [[6.6. Diffutils-3.8]]
        -   [[6.7. File-5.41]]
        -   [[6.8. Findutils-4.9.0]]
        -   [[6.9. Gawk-5.1.1]]
        -   [[6.10. Grep-3.7]]
        -   [[6.11. Gzip-1.11]]
        -   [[6.12. Make-4.3]]
        -   [[6.13. Patch-2.7.6]]
        -   [[6.14. Sed-4.8]]
        -   [[6.15. Tar-1.34]]
        -   [[6.16. Xz-5.2.5]]
        -   [[6.17. Binutils-2.38 - Pass 2]]
        -   [[6.18. GCC-11.2.0 - Pass 2]]
    -   7. Entering Chroot and Building Additional Temporary Tools
        -   [[7.1. Chapter 7 Introduction]]
        -   [[7.2. Changing Ownership]]
        -   [[7.3. Preparing Virtual Kernel File Systems]]
        -   [[7.4. Entering the Chroot Environment]]
        -   [[7.5. Creating Directories]]
        -   [[7.6. Creating Essential Files and Symlinks]]
        -   [[7.7. Libstdc++ from GCC-11.2.0, Pass 2]]
        -   [[7.8. Gettext-0.21]]
        -   [[7.9. Bison-3.8.2]]
        -   [[7.10. Perl-5.34.0]]
        -   [[7.11.Python-3.10.2]]
        -   [[7.12. Texinfo-6.8]]
        -   [[7.13. Util-linux-2.37.4]]
        -   [[7.14. Cleaning up and Saving the Temporary System]]
-   IV. Building the LFS System
    -   8. Installing Basic System Software
        -   [[8.1. Chapter 8 Introduction]]
        -   [[8.2. Package Management]]
        -   [[8.3. Man-pages-5.13]]
        -   [[8.4. Iana-Etc-20220207]]
        -   [[8.5. Glibc-2.35]]
        -   [[8.6. Zlib-1.2.11]]
        -   [[8.7. Bzip2-1.0.8]]
        -   [[8.8. Xz-5.2.5]]
        -   [[8.9. Zstd-1.5.2]]
        -   [[8.10. File-5.41]]
        -   [[8.11. Readline-8.1.2]]
        -   [[8.12. M4-1.4.19]]
        -   [[8.13. Bc-5.2.2]]
        -   [[8.14. Flex-2.6.4]]
        -   [[8.15. Tcl-8.6.12]]
        -   [[8.16. Expect-5.45.4]]
        -   [[8.17. DejaGNU-1.6.3]]
        -   [[8.18. Binutils-2.38]]
        -   [[8.19. GMP-6.2.1]]
        -   [[8.20. MPFR-4.1.0]]
        -   [[8.21. MPC-1.2.1]]
        -   [[8.22. Attr-2.5.1]]
        -   [[8.23. Acl-2.3.1]]
        -   [[8.24. Libcap-2.63]]
        -   [[8.25. Shadow-4.11.1]]
        -   [[8.26. GCC-11.2.0]]
        -   [[8.27. Pkg-config-0.29.2]]
        -   [[8.28. Ncurses-6.3]]
        -   [[8.29. Sed-4.8]]
        -   [[8.30. Psmisc-23.4]]
        -   [[8.31. Gettext-0.21]]
        -   [[8.32. Bison-3.8.2]]
        -   [[8.33. Grep-3.7]]
        -   [[8.34. Bash-5.1.16]]
        -   [[8.35. Libtool-2.4.6]]
        -   [[8.36. GDBM-1.23]]
        -   [[8.37. Gperf-3.1]]
        -   [[8.38. Expat-2.4.6]]
        -   [[8.39. Inetutils-2.2]]
        -   [[8.40. Less-590]]
        -   [[8.41. Perl-5.34.0]]
        -   [[8.42. XML Parser-2.46]]
        -   [[8.43. Intltool-0.51.0]]
        -   [[8.44. Autoconf-2.71]]
        -   [[8.45. Automake-1.16.5]]
        -   [[8.46. OpenSSL-3.0.1]]
        -   [[8.47. Kmod-29]]
        -   [[8.48. Libelf from Elfutils-0.186]]
        -   [[8.49. Libffi-3.4.2]]
        -   [[8.50. Python-3.10.2]]
        -   [[8.51. Ninja-1.10.2]]
        -   [[8.52. Meson-0.61.1]]
        -   [[8.53. Coreutils-9.0]]
        -   [[8.54. Check-0.15.2]]
        -   [[8.55. Diffutils-3.8]]
        -   [[8.56. Gawk-5.1.1]]
        -   [[8.57. Findutils-4.9.0]]
        -   [[8.58. Groff-1.22.4]]
        -   [[8.59. GRUB-2.06]]
        -   [[8.60. Gzip-1.11]]
        -   [[8.61. IPRoute2-5.16.0]]
        -   [[8.62. Kbd-2.4.0]]
        -   [[8.63. Libpipeline-1.5.5]]
        -   [[8.64. Make-4.3]]
        -   [[8.65. Patch-2.7.6]]
        -   [[8.66. Tar-1.34]]
        -   [[8.67. Texinfo-6.8]]
        -   [[8.68. Vim-8.2.4383]]
        -   [[8.69. Eudev-3.2.11]]
        -   [[8.70. Man-DB-2.10.1]]
        -   [[8.71. Procps-ng-3.3.17]]
        -   [[8.72. Util-linux-2.37.4]]
        -   [[8.73. E2fsprogs-1.46.5]]
        -   [[8.74. Sysklogd-1.5.1]]
        -   [[8.75. Sysvinit-3.01]]
        -   [[8.76. About Debugging Symbols]]
        -   [[8.77. Stripping]]
        -   [[8.78. Cleaning Up]]
    -   9. System Configuration
        -   [[9.1. Chapter 9 Introduction]]
        -   [[9.2. LFS-Bootscripts-20210608]]
        -   [[9.3. Overview of Device and Module Handling]]
        -   [[9.4. Managing Devices]]
        -   [[9.5. General Network Configuration]]
        -   [[9.6. System V Bootscript Usage and Configuration]]
        -   [[9.7. The Bash Shell Startup Files]]
        -   [[9.8. Inputrc File]]
        -   [[9.9. Shells File]]
    -   10. Making the LFS System Bootable
        -   [[10.1. Chapter 10 Introduction]]
        -   [[10.2 fstab File]]
        -   [[10.3. Linux-5.16.9]]
        -   [[10.4. Using GRUB to Set Up the Boot Process]]
    -   11. The End
        -   [[11.1. The End]]
        -   [[11.2. Get Counted]]
        -   [[11.3. Rebooting the System]]
        -   [[11.4. What Now]]
-   V. Appendices
    -   [A. Acronyms and Terms](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#appendixa)
    -   [B. Acknowledgments](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#appendixb)
    -   [C. Dependencies](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#appendixc)
    -   [D. Boot and sysconfig scripts version-20210608](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#scripts)
        -   [/etc/rc.d/init.d/rc](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#rc)
        -   [/lib/lsb/init-functions](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#init-functions)
        -   [/etc/rc.d/init.d/mountvirtfs](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#mountvirtfs)
        -   [/etc/rc.d/init.d/modules](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#modules)
        -   [/etc/rc.d/init.d/udev](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#udev)
        -   [/etc/rc.d/init.d/swap](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#swap)
        -   [/etc/rc.d/init.d/setclock](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#setclock)
        -   [/etc/rc.d/init.d/checkfs](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#checkfs)
        -   [/etc/rc.d/init.d/mountfs](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#mountfs)
        -   [/etc/rc.d/init.d/udev_retry](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#udev_retry)
        -   [/etc/rc.d/init.d/cleanfs](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#cleanfs)
        -   [/etc/rc.d/init.d/console](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#console)
        -   [/etc/rc.d/init.d/localnet](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#localnet)
        -   [/etc/rc.d/init.d/sysctl](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#sysctlscript)
        -   [/etc/rc.d/init.d/sysklogd](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#sysklogd)
        -   [/etc/rc.d/init.d/network](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#network)
        -   [/etc/rc.d/init.d/sendsignals](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#sendsignals)
        -   [/etc/rc.d/init.d/reboot](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#rebootscript)
        -   [/etc/rc.d/init.d/halt](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#haltscript)
        -   [/etc/rc.d/init.d/template](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#template)
        -   [/etc/sysconfig/modules](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#modulessys)
        -   [/etc/sysconfig/createfiles](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#createfiles)
        -   [/etc/sysconfig/udev-retry](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#config-udev-retry)
        -   [/sbin/ifup](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ifup)
        -   [/sbin/ifdown](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ifdown)
        -   [/lib/services/ipv4-static](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ipv4static)
        -   [/lib/services/ipv4-static-route](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ipv4route)
    -   [E. Udev configuration rules](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#rules)
        -   [55-lfs.rules](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#lfsrules)
    -   [F. LFS Licenses](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#Licenses)
        -   [Creative Commons License](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#CC)
        -   [The MIT License](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#MIT)
-   [[Index]]