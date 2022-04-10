## 5.3. GCC-11.2.0 - Pass 1

The GCC package contains the GNU compiler collection, which includes the C and C++ compilers.

**Approximate build time:**11 SBU

**Required disk space:**3.3 GB

### 5.3.1. Installation of Cross GCC

GCC requires the GMP, MPFR and MPC packages. As these packages may not be included in your host distribution, they will be built with GCC. Unpack each package into the GCC source directory and rename the resulting directories so the GCC build procedures will automatically use them:

### Note

There are frequent misunderstandings about this chapter. The procedures are the same as every other chapter as explained earlier ([Package build instructions](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#buildinstr)). First extract the gcc tarball from the sources directory and then change to the directory created. Only then should you proceed with the instructions below.

tar -xf ../mpfr-4.1.0.tar.xz
mv -v mpfr-4.1.0 mpfr
tar -xf ../gmp-6.2.1.tar.xz
mv -v gmp-6.2.1 gmp
tar -xf ../mpc-1.2.1.tar.gz
mv -v mpc-1.2.1 mpc

On x86_64 hosts, set the default directory name for 64-bit libraries to “lib”:

case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
 ;;
esac

The GCC documentation recommends building GCC in a dedicated build directory:

mkdir -v build
cd       build

Prepare GCC for compilation:

../configure                  \
    --target=$LFS_TGT         \
    --prefix=$LFS/tools       \
    --with-glibc-version=2.35 \
    --with-sysroot=$LFS       \
    --with-newlib             \
    --without-headers         \
    --enable-initfini-array   \
    --disable-nls             \
    --disable-shared          \
    --disable-multilib        \
    --disable-decimal-float   \
    --disable-threads         \
    --disable-libatomic       \
    --disable-libgomp         \
    --disable-libquadmath     \
    --disable-libssp          \
    --disable-libvtv          \
    --disable-libstdcxx       \
    --enable-languages=c,c++

**The meaning of the configure options:**

_`--with-glibc-version=2.35`_

This option specifies the version of glibc which will be used on the target. It is not relevant to the libc of the host distro because everything compiled by pass1 gcc will run in the chroot environment, which is isolated from libc of the host distro.

_`--with-newlib`_

Since a working C library is not yet available, this ensures that the inhibit_libc constant is defined when building libgcc. This prevents the compiling of any code that requires libc support.

_`--without-headers`_

When creating a complete cross-compiler, GCC requires standard headers compatible with the target system. For our purposes these headers will not be needed. This switch prevents GCC from looking for them.

_`--enable-initfini-array`_

This switch forces the use of some internal data structures that are needed but cannot be detected when building a cross compiler.

_`--disable-shared`_

This switch forces GCC to link its internal libraries statically. We need this because the shared libraries require glibc, which is not yet installed on the target system.

_`--disable-multilib`_

On x86_64, LFS does not support a multilib configuration. This switch is harmless for x86.

_`--disable-decimal-float, --disable-threads, --disable-libatomic, --disable-libgomp, --disable-libquadmath, --disable-libssp, --disable-libvtv, --disable-libstdcxx`_

These switches disable support for the decimal floating point extension, threading, libatomic, libgomp, libquadmath, libssp, libvtv, and the C++ standard library respectively. These features will fail to compile when building a cross-compiler and are not necessary for the task of cross-compiling the temporary libc.

_`--enable-languages=c,c++`_

This option ensures that only the C and C++ compilers are built. These are the only languages needed now.

Compile GCC by running:

make

Install the package:

make install

This build of GCC has installed a couple of internal system headers. Normally one of them, `limits.h`, would in turn include the corresponding system `limits.h` header, in this case, `$LFS/usr/include/limits.h`. However, at the time of this build of GCC `$LFS/usr/include/limits.h` does not exist, so the internal header that has just been installed is a partial, self-contained file and does not include the extended features of the system header. This is adequate for building glibc, but the full internal header will be needed later. Create a full version of the internal header using a command that is identical to what the GCC build system does in normal circumstances:

cd ..
cat gcc/limitx.h gcc/glimits.h gcc/limity.h > \
  `dirname $($LFS_TGT-gcc -print-libgcc-file-name)`/install-tools/include/limits.h

Details on this package are located in [Section 8.26.2, “Contents of GCC.”](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#contents-gcc "8.26.2. Contents of GCC")