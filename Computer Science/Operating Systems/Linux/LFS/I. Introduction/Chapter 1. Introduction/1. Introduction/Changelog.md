## 1.3. Changelog

This is version 11.1 of the Linux From Scratch book, dated March 1st, 2022. If this book is more than six months old, a newer and better version is probably already available. To find out, please check one of the mirrors via [https://www.linuxfromscratch.org/mirrors.html](https://www.linuxfromscratch.org/mirrors.html).

Below is a list of changes made since the previous release of the book.

**Changelog Entries:**

-   2022-03-01
    
    -   [bdubbs] - LFS-11.1 released.
        
    
-   2022-02-23
    
    -   [bdubbs] - Update to expat-2.4.6 (security fix). Fixes [#5011](https://wiki.linuxfromscratch.org/lfs/ticket/5011).
        
    
-   2022-02-15
    
    -   [bdubbs] - LFS-11.1-rc1 released.
        
    -   [bdubbs] - Add binutils-2.38 LTO patch. Fixes [#5011](https://wiki.linuxfromscratch.org/lfs/ticket/5011).
        
    -   [bdubbs] - Update to util-linux-2.37.4. Fixes [#5010](https://wiki.linuxfromscratch.org/lfs/ticket/5010).
        
    -   [bdubbs] - Update to man-db-2.10.1. Fixes [#5009](https://wiki.linuxfromscratch.org/lfs/ticket/5009).
        
    -   [bdubbs] - Update to linux-5.16.9. Fixes [#5008](https://wiki.linuxfromscratch.org/lfs/ticket/5008).
        
    -   [bdubbs] - Update to vim-8.2.4383 (Security Update). Addresses [#4500](https://wiki.linuxfromscratch.org/lfs/ticket/4500).
        
    -   [bdubbs] - Update to iana-etc-20220207. Addresses [#5006](https://wiki.linuxfromscratch.org/lfs/ticket/5006).
        
    
-   2022-02-10
    
    -   [xry111] - Workaround the issue causing binaries link to libraries from the host distro for pass 2 binutils. It's now unnecessary to build zlib in chapter 6.
        
    
-   2022-02-09
    
    -   [bdubbs] - Update to bc-5.2.2. Fixes [#5004](https://wiki.linuxfromscratch.org/lfs/ticket/5004).
        
    -   [bdubbs] - Update to linux-5.16.8. Fixes [#5005](https://wiki.linuxfromscratch.org/lfs/ticket/5005).
        
    -   [bdubbs] - Update to binutils-2.38. Requires adding zlib to Chapter 6. Fixes [#5007](https://wiki.linuxfromscratch.org/lfs/ticket/5007).
        
    
-   2022-02-04
    
    -   [xry111] - Remove **bash** `+h` directives in chroot. Fixes [#4998](https://wiki.linuxfromscratch.org/lfs/ticket/4998).
        
    -   [xry111] - Update to man-db-2.10.0. Fixes [#5002](https://wiki.linuxfromscratch.org/lfs/ticket/5002).
        
    -   [xry111] - Move OpenSSL before Kmod and enable OpenSSL for Kmod build.
        
    -   [xry111] - Update to gdbm-1.23. Fixes [#5000](https://wiki.linuxfromscratch.org/lfs/ticket/5000).
        
    -   [xry111] - Update to tcl-8.6.12. Fixes [#5001](https://wiki.linuxfromscratch.org/lfs/ticket/5001).
        
    -   [thomas] - Remove sed from glibc instructions in chapter 8. It has been applied upstream.
        
    
-   2022-02-03
    
    -   [bdubbs] - Add coreutils-9.0 chmod patch. Fixes [#4992](https://wiki.linuxfromscratch.org/lfs/ticket/4992).
        
    -   [bdubbs] - Update to glibc-2.35. Fixes [#4999](https://wiki.linuxfromscratch.org/lfs/ticket/4999).
        
    -   [bdubbs] - Update to linux-5.16.5. Fixes [#4996](https://wiki.linuxfromscratch.org/lfs/ticket/4996).
        
    -   [bdubbs] - Update to findutils-4.9.0. Fixes [#4995](https://wiki.linuxfromscratch.org/lfs/ticket/4995).
        
    -   [bdubbs] - Update to expat-2.4.4. Fixes [#4993](https://wiki.linuxfromscratch.org/lfs/ticket/4993).
        
    -   [bdubbs] - Update to iana-etc-20220128. Fixes [#4994](https://wiki.linuxfromscratch.org/lfs/ticket/4994).
        
    
-   2022-01-29
    
    -   [bdubbs] - Update to linux-5.16.4. Fixes [#4991](https://wiki.linuxfromscratch.org/lfs/ticket/4991).
        
    
-   2022-01-27
    
    -   [bdubbs] - Update to vim-8.2.4236. Addresses [#4500](https://wiki.linuxfromscratch.org/lfs/ticket/4500).
        
    -   [bdubbs] - Update to zstd-1.5.2. Fixes [#4988](https://wiki.linuxfromscratch.org/lfs/ticket/4988).
        
    -   [bdubbs] - Update to util-linux-2.37.3 (security fix). Fixes [#4989](https://wiki.linuxfromscratch.org/lfs/ticket/4989).
        
    -   [bdubbs] - Update to Python-3.10.2. Fixes [#4987](https://wiki.linuxfromscratch.org/lfs/ticket/4987).
        
    -   [bdubbs] - Update to linux-5.16.2. Fixes [#4979](https://wiki.linuxfromscratch.org/lfs/ticket/4979).
        
    -   [bdubbs] - Update to libcap-2.63. Fixes [#4990](https://wiki.linuxfromscratch.org/lfs/ticket/4990).
        
    -   [bdubbs] - Update to iproute2-5.16.0. Fixes [#4982](https://wiki.linuxfromscratch.org/lfs/ticket/4982).
        
    -   [bdubbs] - Update to iana-etc-20220120. Fixes [#4975](https://wiki.linuxfromscratch.org/lfs/ticket/4975).
        
    
-   2022-01-20
    
    -   [bdubbs] - Update to expat-2.4.3 (security fixes). Fixes [#4984](https://wiki.linuxfromscratch.org/lfs/ticket/4984).
        
    -   [pierre] - Update to meson-0.61.1. Fixes [#4985](https://wiki.linuxfromscratch.org/lfs/ticket/4985).
        
    
-   2022-01-17
    
    -   [thomas] - Added a fix of a typo to the meson-0.61.0 patch.
        
    
-   2022-01-15
    
    -   [bdubbs] - Update to shadow-4.11.1. Fixes [#4976](https://wiki.linuxfromscratch.org/lfs/ticket/4976).
        
    -   [bdubbs] - Update to readline-8.1.2. Fixes [#4980](https://wiki.linuxfromscratch.org/lfs/ticket/4980).
        
    -   [bdubbs] - Update to meson-0.61.0. Fixes [#4983](https://wiki.linuxfromscratch.org/lfs/ticket/4983).
        
    -   [bdubbs] - Update to libpipeline-1.5.5. Fixes [#4977](https://wiki.linuxfromscratch.org/lfs/ticket/4977).
        
    -   [bdubbs] - Update to bash-5.1.16. Fixes [#4978](https://wiki.linuxfromscratch.org/lfs/ticket/4978).
        
    
-   2022-01-01
    
    -   [bdubbs] - Update to e2fsprogs-1.46.5. Fixes [#4974](https://wiki.linuxfromscratch.org/lfs/ticket/4974).
        
    -   [bdubbs] - Update to zstd-1.5.1. Fixes [#4972](https://wiki.linuxfromscratch.org/lfs/ticket/4972).
        
    -   [bdubbs] - Update to expat-2.4.2. Fixes [#4970](https://wiki.linuxfromscratch.org/lfs/ticket/4970).
        
    -   [bdubbs] - Update to shadow-4.10. Fixes [#4969](https://wiki.linuxfromscratch.org/lfs/ticket/4969).
        
    -   [bdubbs] - Update to sysvinit-3.01. Fixes [#4968](https://wiki.linuxfromscratch.org/lfs/ticket/4968).
        
    -   [bdubbs] - Update to linux-5.15.12. Fixes [#4967](https://wiki.linuxfromscratch.org/lfs/ticket/4967).
        
    -   [bdubbs] - Update to iana-etc-20211224. Fixes [#4962](https://wiki.linuxfromscratch.org/lfs/ticket/4962).
        
    -   [bdubbs] - Update to openssl-3.0.1. Fixes [#4922](https://wiki.linuxfromscratch.org/lfs/ticket/4922).
        
    -   [bdubbs] - Update to eudev-3.2.11. Fixes [#4914](https://wiki.linuxfromscratch.org/lfs/ticket/4914).
        
    
-   2021-12-30
    
    -   [renodr] - Update to meson-0.60.3. Fixes [#4973](https://wiki.linuxfromscratch.org/lfs/ticket/4973).
        
    
-   2021-12-15
    
    -   [bdubbs] - Update to python3-3.10.1. Fixes [#4963](https://wiki.linuxfromscratch.org/lfs/ticket/4863).
        
    -   [bdubbs] - Update to openssl-1.1.1m. Fixes [#4966](https://wiki.linuxfromscratch.org/lfs/ticket/4866).
        
    -   [bdubbs] - Update to linux-5.15.7. Fixes [#4964](https://wiki.linuxfromscratch.org/lfs/ticket/4864).
        
    -   [bdubbs] - Update to libcap-2.62. Fixes [#4965](https://wiki.linuxfromscratch.org/lfs/ticket/4865).
        
    
-   2021-12-14
    
    -   [thomas] - Allow building findutils on 32 bit systems. Cherry-picked from multilib branch by [pierre].
        
    
-   2021-12-01
    
    -   [bdubbs] - Update to vim-8.2.3704. Addresses [#4500](https://wiki.linuxfromscratch.org/lfs/ticket/4500).
        
    -   [bdubbs] - Update to iana-etc-20211124. Fixes [#4957](https://wiki.linuxfromscratch.org/lfs/ticket/4957).
        
    -   [bdubbs] - Update to bc-5.2.1. Fixes [#4959](https://wiki.linuxfromscratch.org/lfs/ticket/4959).
        
    -   [bdubbs] - Update to meson-0.60.2. Fixes [#4960](https://wiki.linuxfromscratch.org/lfs/ticket/4960).
        
    -   [bdubbs] - Update to linux-5.15.5. Fixes [#4956](https://wiki.linuxfromscratch.org/lfs/ticket/4956).
        
    
-   2021-11-15
    
    -   [bdubbs] - Update to iana-etc-20211112. Fixes [#4955](https://wiki.linuxfromscratch.org/lfs/ticket/4955).
        
    -   [bdubbs] - Update to elfutils-0.186. Fixes [#4954](https://wiki.linuxfromscratch.org/lfs/ticket/4954).
        
    -   [bdubbs] - Update to bc-5.2.0. Fixes [#4952](https://wiki.linuxfromscratch.org/lfs/ticket/4952).
        
    -   [bdubbs] - Update to ncurses-6.3. Fixes [#4951](https://wiki.linuxfromscratch.org/lfs/ticket/4951).
        
    -   [bdubbs] - Update to libpipeline-1.5.4. Fixes [#4950](https://wiki.linuxfromscratch.org/lfs/ticket/4950).
        
    -   [bdubbs] - Update to meson-0.60.1. Fixes [#4949](https://wiki.linuxfromscratch.org/lfs/ticket/4949).
        
    -   [bdubbs] - Update to iproute2-5.15.0. Fixes [#4948](https://wiki.linuxfromscratch.org/lfs/ticket/4948).
        
    -   [bdubbs] - Update to linux-5.15.2. Fixes [#4947](https://wiki.linuxfromscratch.org/lfs/ticket/4947).
        
    
-   2021-11-01
    
    -   [bdubbs] - Update to gawk-5.1.1. Fixes [#4946](https://wiki.linuxfromscratch.org/lfs/ticket/4946).
        
    -   [bdubbs] - Update to meson-0.60.0. Fixes [#4945](https://wiki.linuxfromscratch.org/lfs/ticket/4945).
        
    -   [bdubbs] - Update to libcap-2.60. Fixes [#4944](https://wiki.linuxfromscratch.org/lfs/ticket/4944).
        
    -   [bdubbs] - Update to gdbm-1.22. Fixes [#4943](https://wiki.linuxfromscratch.org/lfs/ticket/4943).
        
    -   [bdubbs] - Update to file-5.41. Fixes [#4942](https://wiki.linuxfromscratch.org/lfs/ticket/4942).
        
    -   [bdubbs] - Update to linux-5.14.15. Fixes [#4941](https://wiki.linuxfromscratch.org/lfs/ticket/4941).
        
    -   [bdubbs] - Update to iana-etc-20211025. Fixes [#4940](https://wiki.linuxfromscratch.org/lfs/ticket/4940).
        
    -   [bdubbs] - Update to tzdata-2021e. Fixes [#4939](https://wiki.linuxfromscratch.org/lfs/ticket/4939).
        
    
-   2021-10-15
    
    -   [bdubbs] - Update to vim-8.2.3508. Addresses [#4500](https://wiki.linuxfromscratch.org/lfs/ticket/4500).
        
    -   [bdubbs] - Update to tzdata-2021c. Fixes [#4934](https://wiki.linuxfromscratch.org/lfs/ticket/4934).
        
    -   [bdubbs] - Update to Python-3.10.0. Fixes [#4938](https://wiki.linuxfromscratch.org/lfs/ticket/4938).
        
    -   [bdubbs] - Update to Jinja2-3.0.2. Fixes [#4937](https://wiki.linuxfromscratch.org/lfs/ticket/4937).
        
    -   [bdubbs] - Update to linux-5.14.12. Fixes [#4932](https://wiki.linuxfromscratch.org/lfs/ticket/4932).
        
    -   [bdubbs] - Update to iana-etc-20211004. Fixes [#4933](https://wiki.linuxfromscratch.org/lfs/ticket/4933).
        
    -   [bdubbs] - Update to bc-5.1.1. Fixes [#4936](https://wiki.linuxfromscratch.org/lfs/ticket/4936).
        
    -   [bdubbs] - Update to automake-1.16.5. Fixes [#4935](https://wiki.linuxfromscratch.org/lfs/ticket/4935).
        
    
-   2021-10-01
    
    -   [bdubbs] - Update to vim-8.2.3458. Addresses [#4500](https://wiki.linuxfromscratch.org/lfs/ticket/4500).
        
    -   [bdubbs] - Update to iana-etc-20210924. Addresses [#4722](https://wiki.linuxfromscratch.org/lfs/ticket/4722).
        
    -   [bdubbs] - Update to tzdata-2021b. Fixes [#4929](https://wiki.linuxfromscratch.org/lfs/ticket/4929).
        
    -   [bdubbs] - Update to sysvinit-3.0.0. Fixes [#4927](https://wiki.linuxfromscratch.org/lfs/ticket/4927).
        
    -   [bdubbs] - Update to meson-0.59.2. Fixes [#4931](https://wiki.linuxfromscratch.org/lfs/ticket/4931).
        
    -   [bdubbs] - Update to linux-5.14.8. Fixes [#4925](https://wiki.linuxfromscratch.org/lfs/ticket/4925).
        
    -   [bdubbs] - Update to libcap-2.59. Fixes [#4926](https://wiki.linuxfromscratch.org/lfs/ticket/4926).
        
    -   [bdubbs] - Update to coreutils-9.0. Fixes [#4928](https://wiki.linuxfromscratch.org/lfs/ticket/4928).
        
    -   [bdubbs] - Update to bison-3.8.2. Fixes [#4930](https://wiki.linuxfromscratch.org/lfs/ticket/4930).
        
    
-   2021-09-15
    
    -   [bdubbs] - Ensure tcl documentation instructions are present. Fixes [#4923](https://wiki.linuxfromscratch.org/lfs/ticket/4923).
        
    -   [bdubbs] - Update to Python3-3.9.7. Fixes [#4916](https://wiki.linuxfromscratch.org/lfs/ticket/4916).
        
    -   [bdubbs] - Update to linux-5.14.3. Fixes [#4913](https://wiki.linuxfromscratch.org/lfs/ticket/4913).
        
    -   [bdubbs] - Update to libcap-2.57. Fixes [#4912](https://wiki.linuxfromscratch.org/lfs/ticket/4912).
        
    -   [bdubbs] - Update to iproute2-5.14.0. Fixes [#4917](https://wiki.linuxfromscratch.org/lfs/ticket/4917).
        
    -   [bdubbs] - Update to inetutils-2.2. Fixes [#4918](https://wiki.linuxfromscratch.org/lfs/ticket/4918).
        
    -   [bdubbs] - Update to gzip-1.11. Fixes [#4920](https://wiki.linuxfromscratch.org/lfs/ticket/4920).
        
    -   [bdubbs] - Update to gdbm-1.21. Fixes [#4919](https://wiki.linuxfromscratch.org/lfs/ticket/4919).
        
    -   [bdubbs] - Update to bison-3.8.1. Fixes [#4921](https://wiki.linuxfromscratch.org/lfs/ticket/4921).
        
    -   [bdubbs] - Update to bc-5.0.2. Fixes [#4905](https://wiki.linuxfromscratch.org/lfs/ticket/4908).
        
    
-   2021-09-08
    
    -   [renodr] - Fix regressions in File that result in improper detection of text and XZ files.
        
    
-   2021-09-06
    
    -   [bdubbs] - Text clarifications in the backup/restore section of Chapter 7. Thanks to Kevin Buckley for the patch.
        
    
-   2021-09-01
    
    -   [bdubbs] - LFS-11.0 released.
        
    

## 1.4. Resources

### 1.4.1. FAQ

If during the building of the LFS system you encounter any errors, have any questions, or think there is a typo in the book, please start by consulting the Frequently Asked Questions (FAQ) that is located at [https://www.linuxfromscratch.org/faq/](https://www.linuxfromscratch.org/faq/).

### 1.4.2. Mailing Lists

The `linuxfromscratch.org` server hosts a number of mailing lists used for the development of the LFS project. These lists include the main development and support lists, among others. If the FAQ does not solve the problem you are having, the next step would be to search the mailing lists at [https://www.linuxfromscratch.org/search.html](https://www.linuxfromscratch.org/search.html).

For information on the different lists, how to subscribe, archive locations, and additional information, visit [https://www.linuxfromscratch.org/mail.html](https://www.linuxfromscratch.org/mail.html).

### 1.4.3. IRC

Several members of the LFS community offer assistance on Internet Relay Chat (IRC). Before using this support, please make sure that your question is not already answered in the LFS FAQ or the mailing list archives. You can find the IRC network at `irc.libera.chat`. The support channel is named [[lfs-support]].

### 1.4.4. Mirror Sites

The LFS project has a number of world-wide mirrors to make accessing the website and downloading the required packages more convenient. Please visit the LFS website at [https://www.linuxfromscratch.org/mirrors.html](https://www.linuxfromscratch.org/mirrors.html) for a list of current mirrors.

### 1.4.5. Contact Information

Please direct all your questions and comments to one of the LFS mailing lists (see above).