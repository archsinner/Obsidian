## Rationale for Packages in the Book

As stated earlier, the goal of LFS is to build a complete and usable foundation-level system. This includes all packages needed to replicate itself while providing a relatively minimal base from which to customize a more complete system based on the choices of the user. This does not mean that LFS is the smallest system possible. Several important packages are included that are not strictly required. The lists below document the rationale for each package in the book.

-   Acl
    
    This package contains utilities to administer Access Control Lists, which are used to define more fine-grained discretionary access rights for files and directories.
    
-   Attr
    
    This package contains programs for administering extended attributes on filesystem objects.
    
-   Autoconf
    
    This package contains programs for producing shell scripts that can automatically configure source code from a developer's template. It is often needed to rebuild a package after updates to the build procedures.
    
-   Automake
    
    This package contains programs for generating Make files from a template. It is often needed to rebuild a package after updates to the build procedures.
    
-   Bash
    
    This package satisfies an LSB core requirement to provide a Bourne Shell interface to the system. It was chosen over other shell packages because of its common usage and extensive capabilities beyond basic shell functions.
    
-   Bc
    
    This package provides an arbitrary precision numeric processing language. It satisfies a requirement needed when building the Linux kernel.
    
-   Binutils
    
    This package contains a linker, an assembler, and other tools for handling object files. The programs in this package are needed to compile most of the packages in an LFS system and beyond.
    
-   Bison
    
    This package contains the GNU version of yacc (Yet Another Compiler Compiler) needed to build several other LFS programs.
    
-   Bzip2
    
    This package contains programs for compressing and decompressing files. It is required to decompress many LFS packages.
    
-   Check
    
    This package contains a test harness for other programs.
    
-   Coreutils
    
    This package contains a number of essential programs for viewing and manipulating files and directories. These programs are needed for command line file management, and are necessary for the installation procedures of every package in LFS.
    
-   DejaGNU
    
    This package contains a framework for testing other programs.
    
-   Diffutils
    
    This package contains programs that show the differences between files or directories. These programs can be used to create patches, and are also used in many packages' build procedures.
    
-   E2fsprogs
    
    This package contains the utilities for handling the ext2, ext3 and ext4 file systems. These are the most common and thoroughly tested file systems that Linux supports.
    
-   Eudev
    
    This package is a device manager. It dynamically controls the ownership, permissions, names, and symbolic links of devices in the /dev directory as devices are added or removed from the system.
    
-   Expat
    
    This package contains a relatively small XML parsing library. It is required by the XML::Parser Perl module.
    
-   Expect
    
    This package contains a program for carrying out scripted dialogues with other interactive programs. It is commonly used for testing other packages.
    
-   File
    
    This package contains a utility for determining the type of a given file or files. A few packages need it in their build scripts.
    
-   Findutils
    
    This package contains programs to find files in a file system. It is used in many packages' build scripts.
    
-   Flex
    
    This package contains a utility for generating programs that recognize patterns in text. It is the GNU version of the lex (lexical analyzer) program. It is required to build several LFS packages.
    
-   Gawk
    
    This package contains programs for manipulating text files. It is the GNU version of awk (Aho-Weinberg-Kernighan). It is used in many other packages' build scripts.
    
-   GCC
    
    This package is the Gnu Compiler Collection. It contains the C and C++ compilers as well as several others not built by LFS.
    
-   GDBM
    
    This package contains the GNU Database Manager library. It is used by one other LFS package, Man-DB.
    
-   Gettext
    
    This package contains utilities and libraries for internationalization and localization of numerous packages.
    
-   Glibc
    
    This package contains the main C library. Linux programs will not run without it.
    
-   GMP
    
    This package contains math libraries that provide useful functions for arbitrary precision arithmetic. It is required to build GCC.
    
-   Gperf
    
    This package contains a program that generates a perfect hash function from a key set. It is required for Eudev.
    
-   Grep
    
    This package contains programs for searching through files. These programs are used by most packages' build scripts.
    
-   Groff
    
    This package contains programs for processing and formatting text. One important function of these programs is to format man pages.
    
-   GRUB
    
    This package is the Grand Unified Boot Loader. It is one of several boot loaders available, but is the most flexible.
    
-   Gzip
    
    This package contains programs for compressing and decompressing files. It is needed to decompress many packages in LFS and beyond.
    
-   Iana-etc
    
    This package provides data for network services and protocols. It is needed to enable proper networking capabilities.
    
-   Inetutils
    
    This package contains programs for basic network administration.
    
-   Intltool
    
    This package contains tools for extracting translatable strings from source files.
    
-   IProute2
    
    This package contains programs for basic and advanced IPv4 and IPv6 networking. It was chosen over the other common network tools package (net-tools) for its IPv6 capabilities.
    
-   Kbd
    
    This package contains key-table files, keyboard utilities for non-US keyboards, and a number of console fonts.
    
-   Kmod
    
    This package contains programs needed to administer Linux kernel modules.
    
-   Less
    
    This package contains a very nice text file viewer that allows scrolling up or down when viewing a file. It is also used by Man-DB for viewing manpages.
    
-   Libcap
    
    This package implements the user-space interfaces to the POSIX 1003.1e capabilities available in Linux kernels.
    
-   Libelf
    
    The elfutils project provides libraries and tools for ELF files and DWARF data. Most utilities in this package are available in other packages, but the library is needed to build the Linux kernel using the default (and most efficient) configuration.
    
-   Libffi
    
    This package implements a portable, high level programming interface to various calling conventions. Some programs may not know at the time of compilation what arguments are to be passed to a function. For instance, an interpreter may be told at run-time about the number and types of arguments used to call a given function. Libffi can be used in such programs to provide a bridge from the interpreter program to compiled code.
    
-   Libpipeline
    
    The Libpipeline package contains a library for manipulating pipelines of subprocesses in a flexible and convenient way. It is required by the Man-DB package.
    
-   Libtool
    
    This package contains the GNU generic library support script. It wraps the complexity of using shared libraries in a consistent, portable interface. It is needed by the test suites in other LFS packages.
    
-   Linux Kernel
    
    This package is the Operating System. It is the Linux in the GNU/Linux environment.
    
-   M4
    
    This package contains a general text macro processor useful as a build tool for other programs.
    
-   Make
    
    This package contains a program for directing the building of packages. It is required by almost every package in LFS.
    
-   Man-DB
    
    This package contains programs for finding and viewing man pages. It was chosen instead of the man package due to superior internationalization capabilities. It supplies the man program.
    
-   Man-pages
    
    This package contains the actual contents of the basic Linux man pages.
    
-   Meson
    
    This package provides a software tool for automating the building of software. The main goal for Meson is to minimize the amount of time that software developers need to spend configuring their build system. It's required to build Systemd, as well as many BLFS packages.
    
-   MPC
    
    This package contains functions for the arithmetic of complex numbers. It is required by GCC.
    
-   MPFR
    
    This package contains functions for multiple precision arithmetic. It is required by GCC.
    
-   Ninja
    
    This package contains a small build system with a focus on speed. It is designed to have its input files generated by a higher-level build system, and to run builds as fast as possible. This package is required by Meson.
    
-   Ncurses
    
    This package contains libraries for terminal-independent handling of character screens. It is often used to provide cursor control for a menuing system. It is needed by a number of packages in LFS.
    
-   Openssl
    
    This package provides management tools and libraries relating to cryptography. These are useful for providing cryptographic functions to other packages, including the Linux kernel.
    
-   Patch
    
    This package contains a program for modifying or creating files by applying a _patch_ file typically created by the diff program. It is needed by the build procedure for several LFS packages.
    
-   Perl
    
    This package is an interpreter for the runtime language PERL. It is needed for the installation and test suites of several LFS packages.
    
-   Pkg-config
    
    This package provides a program that returns meta-data about an installed library or package.
    
-   Procps-NG
    
    This package contains programs for monitoring processes. These programs are useful for system administration, and are also used by the LFS Bootscripts.
    
-   Psmisc
    
    This package contains programs for displaying information about running processes. These programs are useful for system administration.
    
-   Python 3
    
    This package provides an interpreted language that has a design philosophy that emphasizes code readability.
    
-   Readline
    
    This package is a set of libraries that offers command-line editing and history capabilities. It is used by Bash.
    
-   Sed
    
    This package allows editing of text without opening it in a text editor. It is also needed by most LFS packages' configure scripts.
    
-   Shadow
    
    This package contains programs for handling passwords in a secure way.
    
-   Sysklogd
    
    This package contains programs for logging system messages, such as those given by the kernel or daemon processes when unusual events occur.
    
-   Sysvinit
    
    This package provides the init program, which is the parent of all other processes on the Linux system.
    
-   Tar
    
    This package provides archiving and extraction capabilities of virtually all packages used in LFS.
    
-   Tcl
    
    This package contains the Tool Command Language used in many test suites in LFS packages.
    
-   Texinfo
    
    This package contains programs for reading, writing, and converting info pages. It is used in the installation procedures of many LFS packages.
    
-   Util-linux
    
    This package contains miscellaneous utility programs. Among them are utilities for handling file systems, consoles, partitions, and messages.
    
-   Vim
    
    This package contains an editor. It was chosen because of its compatibility with the classic vi editor and its huge number of powerful capabilities. An editor is a very personal choice for many users and any other editor could be substituted if desired.
    
-   XML::Parser
    
    This package is a Perl module that interfaces with Expat.
    
-   XZ Utils
    
    This package contains programs for compressing and decompressing files. It provides the highest compression generally available and is useful for decompressing packages in XZ or LZMA format.
    
-   Zlib
    
    This package contains compression and decompression routines used by some programs.
    
-   Zstd
    
    This package contains compression and decompression routines used by some programs. It provides high compression ratios and a very wide range of compression / speed trade-offs.