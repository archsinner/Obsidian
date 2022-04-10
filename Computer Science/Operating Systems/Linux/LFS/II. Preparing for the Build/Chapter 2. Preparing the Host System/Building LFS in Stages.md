## 2.3. Building LFS in Stages

LFS is designed to be built in one session. That is, the instructions assume that the system will not be shut down during the process. That does not mean that the system has to be done in one sitting. The issue is that certain procedures have to be re-accomplished after a reboot if resuming LFS at different points.

### 2.3.1. Chapters 1–4

These chapters are accomplished on the host system. When restarting, be careful of the following:

-   Procedures done as the `root` user after Section 2.4 need to have the LFS environment variable set _FOR THE ROOT USER_.
    

### 2.3.2. Chapter 5–6

-   The /mnt/lfs partition must be mounted.
    
-   These two chapters _must_ be done as user `lfs`. A **su - lfs** needs to be done before any task in these chapters. Failing to do that, you are at risk of installing packages to the host, and potentially rendering it unusable.
    
-   The procedures in [General Compilation Instructions](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ch-tools-generalinstructions "General Compilation Instructions") are critical. If there is any doubt about installing a package, ensure any previously expanded tarballs are removed, then re-extract the package files, and complete all instructions in that section.
    

### 2.3.3. Chapter 7–10

-   The /mnt/lfs partition must be mounted.
    
-   A few operations, from “Changing Ownership” to “Entering the Chroot Environment” must be done as the `root` user, with the LFS environment variable set for the `root`user.
    
-   When entering chroot, the LFS environment variable must be set for `root`. The LFS variable is not used afterwards.
    
-   The virtual file systems must be mounted. This can be done before or after entering chroot by changing to a host virtual terminal and, as `root`, running the commands in [Section 7.3.2, “Mounting and Populating /dev”](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ch-tools-bindmount "7.3.2. Mounting and Populating /dev") and [Section 7.3.3, “Mounting Virtual Kernel File Systems”](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ch-tools-kernfsmount "7.3.3. Mounting Virtual Kernel File Systems").