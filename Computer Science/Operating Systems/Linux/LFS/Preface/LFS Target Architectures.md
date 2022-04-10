## LFS Target Architectures

The primary target architectures of LFS are the AMD/Intel x86 (32-bit) and x86_64 (64-bit) CPUs. On the other hand, the instructions in this book are also known to work, with some modifications, with the Power PC and ARM CPUs. To build a system that utilizes one of these CPUs, the main prerequisite, in addition to those on the next page, is an existing Linux system such as an earlier LFS installation, Ubuntu, Red Hat/Fedora, SuSE, or other distribution that targets the architecture that you have. Also note that a 32-bit distribution can be installed and used as a host system on a 64-bit AMD/Intel computer.

For building LFS, the gain of building on a 64-bit system compared to a 32-bit system is minimal. For example, in a test build of LFS-9.1 on a Core i7-4790 CPU based system, using 4 cores, the following statistics were measured:

```
Architecture Build Time     Build Size
32-bit       239.9 minutes  3.6 GB
64-bit       233.2 minutes  4.4 GB
```

As you can see, on the same hardware, the 64-bit build is only 3% faster and is 22% larger than the 32-bit build. If you plan to use LFS as a LAMP server, or a firewall, a 32-bit CPU may be largely sufficient. On the other hand, several packages in BLFS now need more than 4GB of RAM to be built and/or to run, so that if you plan to use LFS as a desktop, the LFS authors recommend building on a 64-bit system.

The default 64-bit build that results from LFS is considered a “pure” 64-bit system. That is, it supports 64-bit executables only. Building a “multi-lib” system requires compiling many applications twice, once for a 32-bit system and once for a 64-bit system. This is not directly supported in LFS because it would interfere with the educational objective of providing the instructions needed for a straightforward base Linux system. Some LFS/BLFS editors maintain a fork of LFS for multilib, which is accessible at [https://www.linuxfromscratch.org/~thomas/multilib/index.html](https://www.linuxfromscratch.org/~thomas/multilib/index.html). But it is an advanced topic.