## 5.2. Binutils-2.38 - Pass 1

The Binutils package contains a linker, an assembler, and other tools for handling object files.

**Approximate build time:**1 SBU

**Required disk space:**620 MB

### 5.2.1. Installation of Cross Binutils

### Note

Go back and re-read the notes in the section titled [General Compilation Instructions](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ch-tools-generalinstructions "General Compilation Instructions"). Understanding the notes labeled important can save you a lot of problems later.

It is important that Binutils be the first package compiled because both Glibc and GCC perform various tests on the available linker and assembler to determine which of their own features to enable.

The Binutils documentation recommends building Binutils in a dedicated build directory:

mkdir -v build
cd       build

### Note

In order for the SBU values listed in the rest of the book to be of any use, measure the time it takes to build this package from the configuration, up to and including the first install. To achieve this easily, wrap the commands in a **time** command like this: **`time { ../configure ... && make && make install; }`**.

Now prepare Binutils for compilation:

../configure --prefix=$LFS/tools \
             --with-sysroot=$LFS \
             --target=$LFS_TGT   \
             --disable-nls       \
             --disable-werror

**The meaning of the configure options:**

_`--prefix=$LFS/tools`_

This tells the configure script to prepare to install the binutils programs in the `$LFS/tools` directory.

_`--with-sysroot=$LFS`_

For cross compilation, this tells the build system to look in $LFS for the target system libraries as needed.

`--target=$LFS_TGT`

Because the machine description in the `LFS_TGT` variable is slightly different than the value returned by the **config.guess** script, this switch will tell the **configure** script to adjust binutil's build system for building a cross linker.

_`--disable-nls`_

This disables internationalization as i18n is not needed for the temporary tools.

_`--disable-werror`_

This prevents the build from stopping in the event that there are warnings from the host's compiler.

Continue with compiling the package:

make

Install the package:

make install

Details on this package are located in [Section 8.18.2, “Contents of Binutils.”](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#contents-binutils "8.18.2. Contents of Binutils")