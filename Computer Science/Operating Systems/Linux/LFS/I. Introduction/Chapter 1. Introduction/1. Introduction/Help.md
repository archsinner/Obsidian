## 1.5. Help

If an issue or a question is encountered while working through this book, please check the FAQ page at [https://www.linuxfromscratch.org/faq/#generalfaq](https://www.linuxfromscratch.org/faq/#generalfaq). Questions are often already answered there. If your question is not answered on this page, try to find the source of the problem. The following hint will give you some guidance for troubleshooting: [https://www.linuxfromscratch.org/hints/downloads/files/errors.txt](https://www.linuxfromscratch.org/hints/downloads/files/errors.txt).

If you cannot find your problem listed in the FAQ, search the mailing lists at [https://www.linuxfromscratch.org/search.html](https://www.linuxfromscratch.org/search.html).

We also have a wonderful LFS community that is willing to offer assistance through the mailing lists and IRC (see the [Section 1.4, “Resources”](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ch-intro-resources "1.4. Resources") section of this book). However, we get several support questions every day and many of them can be easily answered by going to the FAQ and by searching the mailing lists first. So, for us to offer the best assistance possible, you need to do some research on your own first. That allows us to focus on the more unusual support needs. If your searches do not produce a solution, please include all relevant information (mentioned below) in your request for help.

### 1.5.1. Things to Mention

Apart from a brief explanation of the problem being experienced, the essential things to include in any request for help are:

-   The version of the book being used (in this case 11.1)
    
-   The host distribution and version being used to create LFS
    
-   The output from the [Host System Requirements](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#version-check) script
    
-   The package or section the problem was encountered in
    
-   The exact error message or symptom being received
    
-   Note whether you have deviated from the book at all
    

### Note

Deviating from this book does _not_ mean that we will not help you. After all, LFS is about personal preference. Being upfront about any changes to the established procedure helps us evaluate and determine possible causes of your problem.

### 1.5.2. Configure Script Problems

If something goes wrong while running the **configure** script, review the `config.log` file. This file may contain errors encountered during **configure** which were not printed to the screen. Include the _relevant_ lines if you need to ask for help.

### 1.5.3. Compilation Problems

Both the screen output and the contents of various files are useful in determining the cause of compilation problems. The screen output from the **configure** script and the **make** run can be helpful. It is not necessary to include the entire output, but do include enough of the relevant information. Below is an example of the type of information to include from the screen output from **make**:

```
gcc -DALIASPATH=\"/mnt/lfs/usr/share/locale:.\"
-DLOCALEDIR=\"/mnt/lfs/usr/share/locale\"
-DLIBDIR=\"/mnt/lfs/usr/lib\"
-DINCLUDEDIR=\"/mnt/lfs/usr/include\" -DHAVE_CONFIG_H -I. -I.
-g -O2 -c getopt1.c
gcc -g -O2 -static -o make ar.o arscan.o commands.o dir.o
expand.o file.o function.o getopt.o implicit.o job.o main.o
misc.o read.o remake.o rule.o signame.o variable.o vpath.o
default.o remote-stub.o version.o opt1.o
-lutil job.o: In function `load_too_high':
/lfs/tmp/make-3.79.1/job.c:1565: undefined reference
to `getloadavg'
collect2: ld returned 1 exit status
make[2]: *** [make] Error 1
make[2]: Leaving directory `/lfs/tmp/make-3.79.1'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/lfs/tmp/make-3.79.1'
make: *** [all-recursive-am] Error 2
```

In this case, many people would just include the bottom section:

```
make [2]: *** [make] Error 1
```

This is not enough information to properly diagnose the problem because it only notes that something went wrong, not _what_ went wrong. The entire section, as in the example above, is what should be saved because it includes the command that was executed and the associated error message(s).

An excellent article about asking for help on the Internet is available online at [http://catb.org/~esr/faqs/smart-questions.html](http://catb.org/~esr/faqs/smart-questions.html). Read and follow the hints in this document to increase the likelihood of getting the help you need.