## 4.6. About the Test Suites

Most packages provide a test suite. Running the test suite for a newly built package is a good idea because it can provide a “sanity check” indicating that everything compiled correctly. A test suite that passes its set of checks usually proves that the package is functioning as the developer intended. It does not, however, guarantee that the package is totally bug free.

Some test suites are more important than others. For example, the test suites for the core toolchain packages—GCC, binutils, and glibc—are of the utmost importance due to their central role in a properly functioning system. The test suites for GCC and glibc can take a very long time to complete, especially on slower hardware, but are strongly recommended.

### Note

Running the test suites in [Chapter 5](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-cross-tools "Chapter 5. Compiling a Cross-Toolchain") and [Chapter 6](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-temporary-tools "Chapter 6. Cross Compiling Temporary Tools") is impossible, since the programs are compiled with a cross-compiler, so are not supposed to be able to run on the build host.

A common issue with running the test suites for binutils and GCC is running out of pseudo terminals (PTYs). This can result in a high number of failing tests. This may happen for several reasons, but the most likely cause is that the host system does not have the `devpts` file system set up correctly. This issue is discussed in greater detail at [https://www.linuxfromscratch.org/lfs/faq.html#no-ptys](https://www.linuxfromscratch.org/lfs/faq.html#no-ptys).

Sometimes package test suites will fail, but for reasons which the developers are aware of and have deemed non-critical. Consult the logs located at [https://www.linuxfromscratch.org/lfs/build-logs/11.1/](https://www.linuxfromscratch.org/lfs/build-logs/11.1/) to verify whether or not these failures are expected. This site is valid for all tests throughout this book.