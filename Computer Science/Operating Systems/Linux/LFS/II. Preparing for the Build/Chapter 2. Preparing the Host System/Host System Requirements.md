## 2.2. Host System Requirements

Your host system should have the following software with the minimum versions indicated. This should not be an issue for most modern Linux distributions. Also note that many distributions will place software headers into separate packages, often in the form of “<package-name>-devel” or “<package-name>-dev”. Be sure to install those if your distribution provides them.

Earlier versions of the listed software packages may work, but have not been tested.

-   **Bash-3.2** (/bin/sh should be a symbolic or hard link to bash)
    
-   **Binutils-2.13.1** (Versions greater than 2.38 are not recommended as they have not been tested)
    
-   **Bison-2.7** (/usr/bin/yacc should be a link to bison or small script that executes bison)
    
-   **Coreutils-6.9**
    
-   **Diffutils-2.8.1**
    
-   **Findutils-4.2.31**
    
-   **Gawk-4.0.1** (/usr/bin/awk should be a link to gawk)
    
-   **GCC-4.8** including the C++ compiler, **g++** (Versions greater than 11.2.0 are not recommended as they have not been tested). C and C++ standard libraries (with headers) must also be present so the C++ compiler can build hosted programs
    
-   **Grep-2.5.1a**
    
-   **Gzip-1.3.12**
    
-   **Linux Kernel-3.2**
    
    The reason for the kernel version requirement is that we specify that version when building glibc in [Chapter 5](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-cross-tools "Chapter 5. Compiling a Cross-Toolchain") and [Chapter 8](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-building-system "Chapter 8. Installing Basic System Software"), at the recommendation of the developers. It is also required by udev.
    
    If the host kernel is earlier than 3.2 you will need to replace the kernel with a more up to date version. There are two ways you can go about this. First, see if your Linux vendor provides a 3.2 or later kernel package. If so, you may wish to install it. If your vendor doesn't offer an acceptable kernel package, or you would prefer not to install it, you can compile a kernel yourself. Instructions for compiling the kernel and configuring the boot loader (assuming the host uses GRUB) are located in [Chapter 10](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-bootable "Chapter 10. Making the LFS System Bootable").
    
-   **M4-1.4.10**
    
-   **Make-4.0**
    
-   **Patch-2.5.4**
    
-   **Perl-5.8.8**
    
-   **Python-3.4**
    
-   **Sed-4.1.5**
    
-   **Tar-1.22**
    
-   **Texinfo-4.7**
    
-   **Xz-5.0.0**
    

### Important

Note that the symlinks mentioned above are required to build an LFS system using the instructions contained within this book. Symlinks that point to other software (such as dash, mawk, etc.) may work, but are not tested or supported by the LFS development team, and may require either deviation from the instructions or additional patches to some packages.

### 

To see whether your host system has all the appropriate versions, and the ability to compile programs, run the following:

cat > version-check.sh << "EOF"
``#!/bin/bash
# Simple script to list version numbers of critical development tools
export LC_ALL=C
bash --version | head -n1 | cut -d" " -f2-4
MYSH=$(readlink -f /bin/sh)
echo "/bin/sh -> $MYSH"
echo $MYSH | grep -q bash || echo "ERROR: /bin/sh does not point to bash"
unset MYSH

echo -n "Binutils: "; ld --version | head -n1 | cut -d" " -f3-
bison --version | head -n1

if [ -h /usr/bin/yacc ]; then
  echo "/usr/bin/yacc -> `readlink -f /usr/bin/yacc`";
elif [ -x /usr/bin/yacc ]; then
  echo yacc is `/usr/bin/yacc --version | head -n1`
else
  echo "yacc not found"
fi

echo -n "Coreutils: "; chown --version | head -n1 | cut -d")" -f2
diff --version | head -n1
find --version | head -n1
gawk --version | head -n1

if [ -h /usr/bin/awk ]; then
  echo "/usr/bin/awk -> `readlink -f /usr/bin/awk`";
elif [ -x /usr/bin/awk ]; then
  echo awk is `/usr/bin/awk --version | head -n1`
else
  echo "awk not found"
fi

gcc --version | head -n1
g++ --version | head -n1
grep --version | head -n1
gzip --version | head -n1
cat /proc/version
m4 --version | head -n1
make --version | head -n1
patch --version | head -n1
echo Perl `perl -V:version`
python3 --version
sed --version | head -n1
tar --version | head -n1
makeinfo --version | head -n1  # texinfo version
xz --version | head -n1

echo 'int main(){}' > dummy.c && g++ -o dummy dummy.c
if [ -x dummy ]
  then echo "g++ compilation OK";
  else echo "g++ compilation failed"; fi
rm -f dummy.c dummy``
EOF

bash version-check.sh