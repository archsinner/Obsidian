## 5.5. Glibc-2.35

The Glibc package contains the main C library. This library provides the basic routines for allocating memory, searching directories, opening and closing files, reading and writing files, string handling, pattern matching, arithmetic, and so on.

**Approximate build time:**4.3 SBU

**Required disk space:**818 MB

### 5.5.1. Installation of Glibc

First, create a symbolic link for LSB compliance. Additionally, for x86_64, create a compatibility symbolic link required for proper operation of the dynamic library loader:

case $(uname -m) in
    i?86)   ln -sfv ld-linux.so.2 $LFS/lib/ld-lsb.so.3
    ;;
    x86_64) ln -sfv ../lib/ld-linux-x86-64.so.2 $LFS/lib64
            ln -sfv ../lib/ld-linux-x86-64.so.2 $LFS/lib64/ld-lsb-x86-64.so.3
    ;;
esac

### Note

The above command is correct. The **ln** command has a few syntactic versions, so be sure to check **info coreutils ln** and `ln(1)` before reporting what you may think is an error.

Some of the Glibc programs use the non-FHS compliant `/var/db` directory to store their runtime data. Apply the following patch to make such programs store their runtime data in the FHS-compliant locations:

patch -Np1 -i ../glibc-2.35-fhs-1.patch

The Glibc documentation recommends building Glibc in a dedicated build directory:

mkdir -v build
cd       build

Ensure that the **ldconfig** and **sln** utilites are installed into `/usr/sbin`:

echo "rootsbindir=/usr/sbin" > configparms

Next, prepare Glibc for compilation:

../configure                             \
      --prefix=/usr                      \
      --host=$LFS_TGT                    \
      --build=$(../scripts/config.guess) \
      --enable-kernel=3.2                \
      --with-headers=$LFS/usr/include    \
      libc_cv_slibdir=/usr/lib

**The meaning of the configure options:**

_`--host=$LFS_TGT, --build=$(../scripts/config.guess)`_

The combined effect of these switches is that Glibc's build system configures itself to be cross-compiled, using the cross-linker and cross-compiler in `$LFS/tools`.

_`--enable-kernel=3.2`_

This tells Glibc to compile the library with support for 3.2 and later Linux kernels. Workarounds for older kernels are not enabled.

_`--with-headers=$LFS/usr/include`_

This tells Glibc to compile itself against the headers recently installed to the $LFS/usr/include directory, so that it knows exactly what features the kernel has and can optimize itself accordingly.

_`libc_cv_slibdir=/usr/lib`_

This ensures that the library is installed in /usr/lib instead of the default /lib64 on 64 bit machines.

During this stage the following warning might appear:

> ```
> configure: WARNING:
> *** These auxiliary programs are missing or
> *** incompatible versions: msgfmt
> *** some features will be disabled.
> *** Check the INSTALL file for required versions.
> ```

The missing or incompatible **msgfmt** program is generally harmless. This **msgfmt** program is part of the Gettext package which the host distribution should provide.

### Note

There have been reports that this package may fail when building as a "parallel make". If this occurs, rerun the make command with a "-j1" option.

Compile the package:

make

Install the package:

### Warning

If `LFS` is not properly set, and despite the recommendations, you are building as `root`, the next command will install the newly built glibc to your host system, which most likely will render it unusable. So double check that the environment is correctly set, before running the following command.

make DESTDIR=$LFS install

**The meaning of the **make install** option:**

_`DESTDIR=$LFS`_

The `DESTDIR` make variable is used by almost all packages to define the location where the package should be installed. If it is not set, it defaults to the root (`/`) directory. Here we specify that the package be installed in `$LFS` , which will become the root after [Section 7.4, “Entering the Chroot Environment”](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ch-tools-chroot "7.4. Entering the Chroot Environment").

Fix hardcoded path to the executable loader in **ldd** script:

sed '/RTLDLIST=/s@/usr@@g' -i $LFS/usr/bin/ldd

### Caution

At this point, it is imperative to stop and ensure that the basic functions (compiling and linking) of the new toolchain are working as expected. To perform a sanity check, run the following commands:

echo 'int main(){}' > dummy.c
$LFS_TGT-gcc dummy.c
readelf -l a.out | grep '/ld-linux'

If everything is working correctly, there should be no errors, and the output of the last command will be of the form:

```
[Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
```

Note that for 32-bit machines, the interpreter name will be `/lib/ld-linux.so.2`.

If the output is not shown as above or there was no output at all, then something is wrong. Investigate and retrace the steps to find out where the problem is and correct it. This issue must be resolved before continuing on.

Once all is well, clean up the test files:

rm -v dummy.c a.out

### Note

Building packages in the next chapter will serve as an additional check that the toolchain has been built properly. If some package, especially binutils-pass2 or gcc-pass2, fails to build, it is an indication that something has gone wrong with the previous Binutils, GCC, or Glibc installations.

Now that our cross-toolchain is complete, finalize the installation of the limits.h header. For doing so, run a utility provided by the GCC developers:

$LFS/tools/libexec/gcc/$LFS_TGT/11.2.0/install-tools/mkheaders

Details on this package are located in [Section 8.5.3, “Contents of Glibc.”](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#contents-glibc "8.5.3. Contents of Glibc")