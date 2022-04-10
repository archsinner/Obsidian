## Toolchain Technical Notes

This section explains some of the rationale and technical details behind the overall build method. It is not essential to immediately understand everything in this section. Most of this information will be clearer after performing an actual build. This section can be referred to at any time during the process.

The overall goal of [Chapter 5](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-cross-tools "Chapter 5. Compiling a Cross-Toolchain") and [Chapter 6](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-temporary-tools "Chapter 6. Cross Compiling Temporary Tools") is to produce a temporary area that contains a known-good set of tools that can be isolated from the host system. By using **chroot**, the commands in the remaining chapters will be contained within that environment, ensuring a clean, trouble-free build of the target LFS system. The build process has been designed to minimize the risks for new readers and to provide the most educational value at the same time.

The build process is based on the process of _cross-compilation_. Cross-compilation is normally used for building a compiler and its toolchain for a machine different from the one that is used for the build. This is not strictly needed for LFS, since the machine where the new system will run is the same as the one used for the build. But cross-compilation has the great advantage that anything that is cross-compiled cannot depend on the host environment.

### About Cross-Compilation

### Note

The LFS book is not, and does not contain a general tutorial to build a cross (or native) toolchain. Don't use the command in the book for a cross toolchain which will be used for some purpose other than building LFS, unless you really understand what you are doing.

Cross-compilation involves some concepts that deserve a section on their own. Although this section may be omitted in a first reading, coming back to it later will be beneficial to your full understanding of the process.

Let us first define some terms used in this context:

build

is the machine where we build programs. Note that this machine is referred to as the “host” in other sections.

host

is the machine/system where the built programs will run. Note that this use of “host” is not the same as in other sections.

target

is only used for compilers. It is the machine the compiler produces code for. It may be different from both build and host.

As an example, let us imagine the following scenario (sometimes referred to as “Canadian Cross”): we may have a compiler on a slow machine only, let's call it machine A, and the compiler ccA. We may have also a fast machine (B), but with no compiler, and we may want to produce code for another slow machine (C). To build a compiler for machine C, we would have three stages:

Stage

Build

Host

Target

Action

1

A

A

B

build cross-compiler cc1 using ccA on machine A

2

A

B

C

build cross-compiler cc2 using cc1 on machine A

3

B

C

C

build compiler ccC using cc2 on machine B

Then, all the other programs needed by machine C can be compiled using cc2 on the fast machine B. Note that unless B can run programs produced for C, there is no way to test the built programs until machine C itself is running. For example, for testing ccC, we may want to add a fourth stage:

Stage

Build

Host

Target

Action

4

C

C

C

rebuild and test ccC using itself on machine C

In the example above, only cc1 and cc2 are cross-compilers, that is, they produce code for a machine different from the one they are run on. The other compilers ccA and ccC produce code for the machine they are run on. Such compilers are called _native_ compilers.

### Implementation of Cross-Compilation for LFS

### Note

Almost all the build systems use names of the form cpu-vendor-kernel-os referred to as the machine triplet. An astute reader may wonder why a “triplet” refers to a four component name. The reason is history: initially, three component names were enough to designate a machine unambiguously, but with new machines and systems appearing, that proved insufficient. The word “triplet” remained. A simple way to determine your machine triplet is to run the **config.guess** script that comes with the source for many packages. Unpack the binutils sources and run the script: **`./config.guess`** and note the output. For example, for a 32-bit Intel processor the output will be _i686-pc-linux-gnu_. On a 64-bit system it will be _x86_64-pc-linux-gnu_.

Also be aware of the name of the platform's dynamic linker, often referred to as the dynamic loader (not to be confused with the standard linker **ld** that is part of binutils). The dynamic linker provided by Glibc finds and loads the shared libraries needed by a program, prepares the program to run, and then runs it. The name of the dynamic linker for a 32-bit Intel machine is `ld-linux.so.2` and is `ld-linux-x86-64.so.2` for 64-bit systems. A sure-fire way to determine the name of the dynamic linker is to inspect a random binary from the host system by running: **`readelf -l <name of binary> | grep interpreter`** and noting the output. The authoritative reference covering all platforms is in the `shlib-versions` file in the root of the Glibc source tree.

In order to fake a cross compilation in LFS, the name of the host triplet is slightly adjusted by changing the "vendor" field in the `LFS_TGT` variable. We also use the _`--with-sysroot`_ option when building the cross linker and cross compiler to tell them where to find the needed host files. This ensures that none of the other programs built in [Chapter 6](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-temporary-tools "Chapter 6. Cross Compiling Temporary Tools") can link to libraries on the build machine. Only two stages are mandatory, and one more for tests:

Stage

Build

Host

Target

Action

1

pc

pc

lfs

build cross-compiler cc1 using cc-pc on pc

2

pc

lfs

lfs

build compiler cc-lfs using cc1 on pc

3

lfs

lfs

lfs

rebuild and test cc-lfs using itself on lfs

In the above table, “on pc” means the commands are run on a machine using the already installed distribution. “On lfs” means the commands are run in a chrooted environment.

Now, there is more about cross-compiling: the C language is not just a compiler, but also defines a standard library. In this book, the GNU C library, named glibc, is used. This library must be compiled for the lfs machine, that is, using the cross compiler cc1. But the compiler itself uses an internal library implementing complex instructions not available in the assembler instruction set. This internal library is named libgcc, and must be linked to the glibc library to be fully functional! Furthermore, the standard library for C++ (libstdc++) also needs being linked to glibc. The solution to this chicken and egg problem is to first build a degraded cc1 based libgcc, lacking some functionalities such as threads and exception handling, then build glibc using this degraded compiler (glibc itself is not degraded), then build libstdc++. But this last library will lack the same functionalities as libgcc.

This is not the end of the story: the conclusion of the preceding paragraph is that cc1 is unable to build a fully functional libstdc++, but this is the only compiler available for building the C/C++ libraries during stage 2! Of course, the compiler built during stage 2, cc-lfs, would be able to build those libraries, but (1) the build system of GCC does not know that it is usable on pc, and (2) using it on pc would be at risk of linking to the pc libraries, since cc-lfs is a native compiler. So we have to build libstdc++ later, in chroot.

### Other procedural details

The cross-compiler will be installed in a separate `$LFS/tools` directory, since it will not be part of the final system.

Binutils is installed first because the **configure** runs of both GCC and Glibc perform various feature tests on the assembler and linker to determine which software features to enable or disable. This is more important than one might first realize. An incorrectly configured GCC or Glibc can result in a subtly broken toolchain, where the impact of such breakage might not show up until near the end of the build of an entire distribution. A test suite failure will usually highlight this error before too much additional work is performed.

Binutils installs its assembler and linker in two locations, `$LFS/tools/bin` and `$LFS/tools/$LFS_TGT/bin`. The tools in one location are hard linked to the other. An important facet of the linker is its library search order. Detailed information can be obtained from **ld** by passing it the _`--verbose`_ flag. For example, **$LFS_TGT-ld --verbose | grep SEARCH** will illustrate the current search paths and their order. It shows which files are linked by **ld** by compiling a dummy program and passing the _`--verbose`_ switch to the linker. For example, **$LFS_TGT-gcc dummy.c -Wl,--verbose 2>&1 | grep succeeded** will show all the files successfully opened during the linking.

The next package installed is GCC. An example of what can be seen during its run of **configure** is:

```
checking what assembler to use... /mnt/lfs/tools/i686-lfs-linux-gnu/bin/as
checking what linker to use... /mnt/lfs/tools/i686-lfs-linux-gnu/bin/ld
```

This is important for the reasons mentioned above. It also demonstrates that GCC's configure script does not search the PATH directories to find which tools to use. However, during the actual operation of **gcc** itself, the same search paths are not necessarily used. To find out which standard linker **gcc** will use, run: **$LFS_TGT-gcc -print-prog-name=ld**.

Detailed information can be obtained from **gcc** by passing it the _`-v`_ command line option while compiling a dummy program. For example, **gcc -v dummy.c** will show detailed information about the preprocessor, compilation, and assembly stages, including **gcc**'s included search paths and their order.

Next installed are sanitized Linux API headers. These allow the standard C library (Glibc) to interface with features that the Linux kernel will provide.

The next package installed is Glibc. The most important considerations for building Glibc are the compiler, binary tools, and kernel headers. The compiler is generally not an issue since Glibc will always use the compiler relating to the _`--host`_ parameter passed to its configure script; e.g. in our case, the compiler will be **$LFS_TGT-gcc**. The binary tools and kernel headers can be a bit more complicated. Therefore, we take no risks and use the available configure switches to enforce the correct selections. After the run of **configure**, check the contents of the `config.make` file in the `build` directory for all important details. Note the use of _`CC="$LFS_TGT-gcc"`_ (with `$LFS_TGT` expanded) to control which binary tools are used and the use of the _`-nostdinc`_ and _`-isystem`_ flags to control the compiler's include search path. These items highlight an important aspect of the Glibc package—it is very self-sufficient in terms of its build machinery and generally does not rely on toolchain defaults.

As said above, the standard C++ library is compiled next, followed in [Chapter 6](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-temporary-tools "Chapter 6. Cross Compiling Temporary Tools") by all the programs that need themselves to be built. The install step of all those packages uses the `DESTDIR` variable to have the programs land into the LFS filesystem.

At the end of [Chapter 6](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-temporary-tools "Chapter 6. Cross Compiling Temporary Tools") the native lfs compiler is installed. First binutils-pass2 is built, with the same `DESTDIR` install as the other programs, then the second pass of GCC is constructed, omitting libstdc++ and other non-important libraries. Due to some weird logic in GCC's configure script, `CC_FOR_TARGET` ends up as **cc** when the host is the same as the target, but is different from the build system. This is why _`CC_FOR_TARGET=$LFS_TGT-gcc`_ is put explicitly into the configure options.

Upon entering the chroot environment in [Chapter 7](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-chroot-temporary-tools "Chapter 7. Entering Chroot and Building Additional Temporary Tools"), the first task is to install libstdc++. Then temporary installations of programs needed for the proper operation of the toolchain are performed. From this point onwards, the core toolchain is self-contained and self-hosted. In [Chapter 8](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-building-system "Chapter 8. Installing Basic System Software"), final versions of all the packages needed for a fully functional system are built, tested and installed.