## 4.4. Setting Up the Environment

Set up a good working environment by creating two new startup files for the **bash** shell. While logged in as user `lfs`, issue the following command to create a new `.bash_profile`:

cat > ~/.bash_profile << "EOF"
`exec env -i HOME=$HOME TERM=$TERM PS1='\u:\w\$ ' /bin/bash`
EOF

When logged on as user `lfs`, the initial shell is usually a _login_ shell which reads the `/etc/profile` of the host (probably containing some settings and environment variables) and then `.bash_profile`. The **exec env -i.../bin/bash** command in the `.bash_profile` file replaces the running shell with a new one with a completely empty environment, except for the `HOME`, `TERM`, and `PS1` variables. This ensures that no unwanted and potentially hazardous environment variables from the host system leak into the build environment. The technique used here achieves the goal of ensuring a clean environment.

The new instance of the shell is a _non-login_ shell, which does not read, and execute, the contents of `/etc/profile` or `.bash_profile` files, but rather reads, and executes, the `.bashrc` file instead. Create the `.bashrc` file now:

cat > ~/.bashrc << "EOF"
`set +h
umask 022
LFS=/mnt/lfs
LC_ALL=POSIX
LFS_TGT=$(uname -m)-lfs-linux-gnu
PATH=/usr/bin
if [ ! -L /bin ]; then PATH=/bin:$PATH; fi
PATH=$LFS/tools/bin:$PATH
CONFIG_SITE=$LFS/usr/share/config.site
export LFS LC_ALL LFS_TGT PATH CONFIG_SITE`
EOF

**The meaning of the settings in `.bashrc`**

_`set +h`_

The **set +h** command turns off **bash**'s hash function. Hashing is ordinarily a useful feature—**bash** uses a hash table to remember the full path of executable files to avoid searching the `PATH` time and again to find the same executable. However, the new tools should be used as soon as they are installed. By switching off the hash function, the shell will always search the `PATH` when a program is to be run. As such, the shell will find the newly compiled tools in `$LFS/tools/bin` as soon as they are available without remembering a previous version of the same program provided by the host distro, in `/usr/bin` or `/bin`.

_`umask 022`_

Setting the user file-creation mask (umask) to 022 ensures that newly created files and directories are only writable by their owner, but are readable and executable by anyone (assuming default modes are used by the `open(2)` system call, new files will end up with permission mode 644 and directories with mode 755).

_`LFS=/mnt/lfs`_

The `LFS` variable should be set to the chosen mount point.

_`LC_ALL=POSIX`_

The `LC_ALL` variable controls the localization of certain programs, making their messages follow the conventions of a specified country. Setting `LC_ALL` to “POSIX” or “C” (the two are equivalent) ensures that everything will work as expected in the chroot environment.

_`LFS_TGT=(uname -m)-lfs-linux-gnu`_

The `LFS_TGT` variable sets a non-default, but compatible machine description for use when building our cross compiler and linker and when cross compiling our temporary toolchain. More information is contained in [Toolchain Technical Notes](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ch-tools-toolchaintechnotes "Toolchain Technical Notes").

_`PATH=/usr/bin`_

Many modern linux distributions have merged `/bin` and `/usr/bin`. When this is the case, the standard `PATH` variable needs just to be set to `/usr/bin/` for the [Chapter 6](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-temporary-tools "Chapter 6. Cross Compiling Temporary Tools") environment. When this is not the case, the following line adds `/bin` to the path.

_`if [ ! -L /bin ]; then PATH=/bin:$PATH; fi`_

If `/bin` is not a symbolic link, then it has to be added to the `PATH` variable.

_`PATH=$LFS/tools/bin:$PATH`_

By putting `$LFS/tools/bin` ahead of the standard `PATH`, the cross-compiler installed at the beginning of [Chapter 5](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-cross-tools "Chapter 5. Compiling a Cross-Toolchain") is picked up by the shell immediately after its installation. This, combined with turning off hashing, limits the risk that the compiler from the host be used instead of the cross-compiler.

_`CONFIG_SITE=$LFS/usr/share/config.site`_

In [Chapter 5](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-cross-tools "Chapter 5. Compiling a Cross-Toolchain") and [Chapter 6](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-temporary-tools "Chapter 6. Cross Compiling Temporary Tools"), if this variable is not set, **configure** scripts may attempt to load configuration items specific to some distributions from `/usr/share/config.site` on the host system. Override it to prevent potential contamination from the host.

_`export ...`_

While the above commands have set some variables, in order to make them visible within any sub-shells, we export them.

### Important

Several commercial distributions add a non-documented instantiation of `/etc/bash.bashrc` to the initialization of **bash**. This file has the potential to modify the `lfs` user's environment in ways that can affect the building of critical LFS packages. To make sure the `lfs` user's environment is clean, check for the presence of `/etc/bash.bashrc` and, if present, move it out of the way. As the `root` user, run:

[ ! -e /etc/bash.bashrc ] || mv -v /etc/bash.bashrc /etc/bash.bashrc.NOUSE

After use of the `lfs` user is finished at the beginning of [Chapter 7](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-chroot-temporary-tools "Chapter 7. Entering Chroot and Building Additional Temporary Tools"), you can restore `/etc/bash.bashrc` (if desired).

Note that the LFS Bash package we will build in [Section 8.34, “Bash-5.1.16”](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ch-system-bash "8.34. Bash-5.1.16") is not configured to load or execute `/etc/bash.bashrc`, so this file is useless on a completed LFS system.

Finally, to have the environment fully prepared for building the temporary tools, source the just-created user profile:

source ~/.bash_profile