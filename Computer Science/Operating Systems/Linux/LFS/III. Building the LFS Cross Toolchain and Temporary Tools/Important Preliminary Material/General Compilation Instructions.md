## General Compilation Instructions

When building packages there are several assumptions made within the instructions:

-   Several of the packages are patched before compilation, but only when the patch is needed to circumvent a problem. A patch is often needed in both this and the following chapters, but sometimes in only one location. Therefore, do not be concerned if instructions for a downloaded patch seem to be missing. Warning messages about _offset_ or _fuzz_ may also be encountered when applying a patch. Do not worry about these warnings, as the patch was still successfully applied.
    
-   During the compilation of most packages, there will be several warnings that scroll by on the screen. These are normal and can safely be ignored. These warnings are as they appear—warnings about deprecated, but not invalid, use of the C or C++ syntax. C standards change fairly often, and some packages still use the older standard. This is not a problem, but does prompt the warning.
    
-   Check one last time that the `LFS` environment variable is set up properly:
    
    echo $LFS
    
    Make sure the output shows the path to the LFS partition's mount point, which is `/mnt/lfs`, using our example.
    
-   Finally, two important items must be emphasized:
    
    ### Important
    
    The build instructions assume that the [Host System Requirements](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#ch-partitioning-hostreqs "2.2. Host System Requirements"), including symbolic links, have been set properly:
    
    -   **bash** is the shell in use.
        
    -   **sh** is a symbolic link to **bash**.
        
    -   **/usr/bin/awk** is a symbolic link to **gawk**.
        
    -   **/usr/bin/yacc** is a symbolic link to **bison** or a small script that executes bison.
        
    
    ### Important
    
    To re-emphasize the build process:
    
    1.  Place all the sources and patches in a directory that will be accessible from the chroot environment such as `/mnt/lfs/sources/`.
        
    2.  Change to the sources directory.
        
    3.  For each package:
        
        1.  Using the **tar** program, extract the package to be built. In [Chapter 5](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-cross-tools "Chapter 5. Compiling a Cross-Toolchain") and [Chapter 6](https://linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-11.1-NOCHUNKS.html#chapter-temporary-tools "Chapter 6. Cross Compiling Temporary Tools"), ensure you are the _lfs_ user when extracting the package.
            
            All methods to get the source code tree being built in-position, except extracting the package tarball, are not supported. Notably, using **cp -R** to copy the source code tree somewhere else can destroy links and timestamps in the sources tree and cause building failure.
            
        2.  Change to the directory created when the package was extracted.
            
        3.  Follow the book's instructions for building the package.
            
        4.  Change back to the sources directory.
            
        5.  Delete the extracted source directory unless instructed otherwise.