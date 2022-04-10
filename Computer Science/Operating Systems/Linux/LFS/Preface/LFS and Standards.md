## LFS and Standards

The structure of LFS follows Linux standards as closely as possible. The primary standards are:

-   [POSIX.1-2008](http://pubs.opengroup.org/onlinepubs/9699919799/).
    
-   [Filesystem Hierarchy Standard (FHS) Version 3.0](http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
    
-   [Linux Standard Base (LSB) Version 5.0 (2015)](http://refspecs.linuxfoundation.org/lsb.shtml)
    
    The LSB has four separate standards: Core, Desktop, Runtime Languages, and Imaging. In addition to generic requirements there are also architecture specific requirements. There are also two areas for trial use: Gtk3 and Graphics. LFS attempts to conform to the architectures discussed in the previous section.
    
    ### Note
    
    Many people do not agree with the requirements of the LSB. The main purpose of defining it is to ensure that proprietary software will be able to be installed and run properly on a compliant system. Since LFS is source based, the user has complete control over what packages are desired and many choose not to install some packages that are specified by the LSB.
    

Creating a complete LFS system capable of passing the LSB certifications tests is possible, but not without many additional packages that are beyond the scope of LFS. These additional packages have installation instructions in BLFS.

#### Packages supplied by LFS needed to satisfy the LSB Requirements

_LSB Core:_

Bash, Bc, Binutils, Coreutils, Diffutils, File, Findutils, Gawk, Grep, Gzip, M4, Man-DB, Ncurses, Procps, Psmisc, Sed, Shadow, Tar, Util-linux, Zlib

_LSB Desktop:_

None

_LSB Runtime Languages:_

Perl, Python

_LSB Imaging:_

None

_LSB Gtk3 and LSB Graphics (Trial Use):_

None

#### Packages supplied by BLFS needed to satisfy the LSB Requirements

_LSB Core:_

At, Batch (a part of At), Cpio, Ed, Fcrontab, LSB-Tools, NSPR, NSS, PAM, Pax, Sendmail (or Postfix or Exim), time

_LSB Desktop:_

Alsa, ATK, Cairo, Desktop-file-utils, Freetype, Fontconfig, Gdk-pixbuf, Glib2, GTK+2, Icon-naming-utils, Libjpeg-turbo, Libpng, Libtiff, Libxml2, MesaLib, Pango, Xdg-utils, Xorg

_LSB Runtime Languages:_

Libxml2, Libxslt

_LSB Imaging:_

CUPS, Cups-filters, Ghostscript, SANE

_LSB Gtk3 and LSB Graphics (Trial Use):_

GTK+3

#### Packages not supplied by LFS or BLFS needed to satisfy the LSB Requirements

_LSB Core:_

None

_LSB Desktop:_

Qt4 (but Qt5 is provided)

_LSB Runtime Languages:_

None

_LSB Imaging:_

None

_LSB Gtk3 and LSB Graphics (Trial Use):_

None