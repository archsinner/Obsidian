## 5.4. Linux-5.16.9 API Headers

The Linux API Headers (in linux-5.16.9.tar.xz) expose the kernel's API for use by Glibc.

**Approximate build time:**0.1 SBU

**Required disk space:**1.2 GB

### 5.4.1. Installation of Linux API Headers

The Linux kernel needs to expose an Application Programming Interface (API) for the system's C library (Glibc in LFS) to use. This is done by way of sanitizing various C header files that are shipped in the Linux kernel source tarball.

Make sure there are no stale files embedded in the package:

make mrproper

Now extract the user-visible kernel headers from the source. The recommended make target “headers_install” cannot be used, because it requires rsync, which may not be available. The headers are first placed in `./usr`, then copied to the needed location.

make headers
find usr/include -name '.*' -delete
rm usr/include/Makefile cp -rv usr/include $LFS/usr

### 5.4.2. Contents of Linux API Headers

**Installed headers:**/usr/include/asm/*.h, /usr/include/asm-generic/*.h, /usr/include/drm/*.h, /usr/include/linux/*.h, /usr/include/misc/*.h, /usr/include/mtd/*.h, /usr/include/rdma/*.h, /usr/include/scsi/*.h, /usr/include/sound/*.h, /usr/include/video/*.h, and /usr/include/xen/*.h

**Installed directories:**/usr/include/asm, /usr/include/asm-generic, /usr/include/drm, /usr/include/linux, /usr/include/misc, /usr/include/mtd, /usr/include/rdma, /usr/include/scsi, /usr/include/sound, /usr/include/video, and /usr/include/xen

#### Short Descriptions

`/usr/include/asm/*.h`

The Linux API ASM Headers

`/usr/include/asm-generic/*.h`

The Linux API ASM Generic Headers

`/usr/include/drm/*.h`

The Linux API DRM Headers

`/usr/include/linux/*.h`

The Linux API Linux Headers

`/usr/include/misc/*.h`

The Linux API Miscellaneous Headers

`/usr/include/mtd/*.h`

The Linux API MTD Headers

`/usr/include/rdma/*.h`

The Linux API RDMA Headers

`/usr/include/scsi/*.h`

The Linux API SCSI Headers

`/usr/include/sound/*.h`

The Linux API Sound Headers

`/usr/include/video/*.h`

The Linux API Video Headers

`/usr/include/xen/*.h`

The Linux API Xen Headers