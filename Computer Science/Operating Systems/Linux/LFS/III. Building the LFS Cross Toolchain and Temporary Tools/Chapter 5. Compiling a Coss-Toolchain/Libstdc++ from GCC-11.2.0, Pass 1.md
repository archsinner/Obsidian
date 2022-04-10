## 5.6. Libstdc++ from GCC-11.2.0, Pass 1

Libstdc++ is the standard C++ library. It is needed to compile C++ code (part of GCC is written in C++), but we had to defer its installation when we built [gcc-pass1](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ch-tools-gcc-pass1 "5.3. GCC-11.2.0 - Pass 1") because it depends on glibc, which was not yet available in the target directory.

**Approximate build time:**0.4 SBU

**Required disk space:**818 MB

### 5.6.1. Installation of Target Libstdc++

### Note

Libstdc++ is part of the GCC sources. You should first unpack the GCC tarball and change to the `gcc-11.2.0` directory.

Create a separate build directory for libstdc++ and enter it:

mkdir -v build
cd       build

Prepare libstdc++ for compilation:

../libstdc++-v3/configure           \
    --host=$LFS_TGT                 \
    --build=$(../config.guess)      \
    --prefix=/usr                   \
    --disable-multilib              \
    --disable-nls                   \
    --disable-libstdcxx-pch         \
    --with-gxx-include-dir=/tools/$LFS_TGT/include/c++/11.2.0

**The meaning of the configure options:**

_`--host=...`_

Specifies that the cross compiler we have just built should be used instead of the one in `/usr/bin`.

_`--disable-libstdcxx-pch`_

This switch prevents the installation of precompiled include files, which are not needed at this stage.

_`--with-gxx-include-dir=/tools/$LFS_TGT/include/c++/11.2.0`_

This specifies the installation directory for include files. Because libstdc++ is the standard C++ library for LFS, this directory should match the location where the C++ compiler (**$LFS_TGT-g++**) would search for the standard C++ include files. In a normal build, this information is automatically passed to the libstdc++ **configure** options from the top level directory. In our case, this information must be explicitly given. The C++ compiler will prepend the sysroot path `$LFS` (specified building GCC pass 1) to the include file search path, so it will actually search in `$LFS/tools/$LFS_TGT/include/c++/11.2.0`. The combination of the _`DESTDIR`_ variable (in the **make install** command below) and this switch ensures to install the headers there.

Compile libstdc++ by running:

make

Install the library:

make DESTDIR=$LFS install

Details on this package are located in [Section 8.26.2, “Contents of GCC.”](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#contents-gcc "8.26.2. Contents of GCC")