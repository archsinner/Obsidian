# I. Introduction

## Chapter 1. Introduction

## 1.1. How to Build an LFS System

The LFS system will be built by using an already installed Linux distribution (such as Debian, OpenMandriva, Fedora, or openSUSE). This existing Linux system (the host) will be used as a starting point to provide necessary programs, including a compiler, linker, and shell, to build the new system. Select the “development” option during the distribution installation to be able to access these tools.

As an alternative to installing a separate distribution onto your machine, you may wish to use a LiveCD from a commercial distribution.

[[Chapter 2 Introduction]] of this book describes how to create a new Linux native partition and file system. This is the place where the new LFS system will be compiled and installed. [Chapter 3](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-getting-materials "Chapter 3. Packages and Patches") explains which packages and patches need to be downloaded to build an LFS system and how to store them on the new file system. [Chapter 4](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-final-preps "Chapter 4. Final Preparations") discusses the setup of an appropriate working environment. Please read [Chapter 4](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-final-preps "Chapter 4. Final Preparations") carefully as it explains several important issues you need be aware of before beginning to work your way through [Chapter 5](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-cross-tools "Chapter 5. Compiling a Cross-Toolchain") and beyond.

[Chapter 5](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-cross-tools "Chapter 5. Compiling a Cross-Toolchain"), explains the installation of the initial tool chain, (binutils, gcc, and glibc) using cross compilation techniques to isolate the new tools from the host system.

[Chapter 6](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-temporary-tools "Chapter 6. Cross Compiling Temporary Tools") shows you how to cross-compile basic utilities using the just built cross-toolchain.

[Chapter 7](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-chroot-temporary-tools "Chapter 7. Entering Chroot and Building Additional Temporary Tools") then enters a "chroot" environment and uses the previously built tools to build the additional tools needed to build and test the final system.

This effort to isolate the new system from the host distribution may seem excessive. A full technical explanation as to why this is done is provided in [Toolchain Technical Notes](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ch-tools-toolchaintechnotes "Toolchain Technical Notes").

In [Chapter 8](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-building-system "Chapter 8. Installing Basic System Software"), The full LFS system is built. Another advantage provided by the chroot environment is that it allows you to continue using the host system while LFS is being built. While waiting for package compilations to complete, you can continue using your computer as normal.

To finish the installation, the basic system configuration is set up in [Chapter 9](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-config "Chapter 9. System Configuration"), and the kernel and boot loader are set up in [Chapter 10](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-bootable "Chapter 10. Making the LFS System Bootable"). [Chapter 11](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-finalizing "Chapter 11. The End") contains information on continuing the LFS experience beyond this book. After the steps in this book have been implemented, the computer will be ready to reboot into the new LFS system.

This is the process in a nutshell. Detailed information on each step is discussed in the following chapters and package descriptions. Items that may seem complicated will be clarified, and everything will fall into place as you embark on the LFS adventure.