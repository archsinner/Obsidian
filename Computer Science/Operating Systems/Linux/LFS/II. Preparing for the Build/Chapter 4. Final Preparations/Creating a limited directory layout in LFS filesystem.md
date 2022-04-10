## 4.2. Creating a limited directory layout in LFS filesystem

The first task performed in the LFS partition is to create a limited directory hierarchy so that programs compiled in [Chapter 6](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-temporary-tools "Chapter 6. Cross Compiling Temporary Tools") (as well as glibc and libstdc++ in [Chapter 5](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-cross-tools "Chapter 5. Compiling a Cross-Toolchain")) may be installed in their final location. This is needed so that those temporary programs be overwritten when rebuilding them in [Chapter 8](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-building-system "Chapter 8. Installing Basic System Software").

Create the required directory layout by running the following as `root`:

mkdir -pv $LFS/{etc,var} $LFS/usr/{bin,lib,sbin}

for i in bin lib sbin; do
  ln -sv usr/$i $LFS/$i
done

case $(uname -m) in
  x86_64) mkdir -pv $LFS/lib64 ;;
esac

Programs in [Chapter 6](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-temporary-tools "Chapter 6. Cross Compiling Temporary Tools") will be compiled with a cross-compiler (more details in section [Toolchain Technical Notes](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ch-tools-toolchaintechnotes "Toolchain Technical Notes")). In order to separate this cross-compiler from the other programs, it will be installed in a special directory. Create this directory with:

mkdir -pv $LFS/tools