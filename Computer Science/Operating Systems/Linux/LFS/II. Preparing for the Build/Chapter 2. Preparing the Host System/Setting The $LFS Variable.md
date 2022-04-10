## 2.6. Setting The $LFS Variable

Throughout this book, the environment variable `LFS` will be used several times. You should ensure that this variable is always defined throughout the LFS build process. It should be set to the name of the directory where you will be building your LFS system - we will use `/mnt/lfs` as an example, but the directory choice is up to you. If you are building LFS on a separate partition, this directory will be the mount point for the partition. Choose a directory location and set the variable with the following command:

export LFS=_`/mnt/lfs`_

Having this variable set is beneficial in that commands such as **mkdir -v $LFS/tools** can be typed literally. The shell will automatically replace “$LFS” with “/mnt/lfs” (or whatever the variable was set to) when it processes the command line.

### Caution

Do not forget to check that `LFS` is set whenever you leave and reenter the current working environment (such as when doing a **su** to `root` or another user). Check that the `LFS` variable is set up properly with:

echo $LFS

Make sure the output shows the path to your LFS system's build location, which is `/mnt/lfs` if the provided example was followed. If the output is incorrect, use the command given earlier on this page to set `$LFS` to the correct directory name.

### Note

One way to ensure that the `LFS` variable is always set is to edit the `.bash_profile` file in both your personal home directory and in `/root/.bash_profile` and enter the export command above. In addition, the shell specified in the `/etc/passwd` file for all users that need the `LFS` variable needs to be bash to ensure that the `/root/.bash_profile` file is incorporated as a part of the login process.

Another consideration is the method that is used to log into the host system. If logging in through a graphical display manager, the user's `.bash_profile` is not normally used when a virtual terminal is started. In this case, add the export command to the `.bashrc` file for the user and `root`. In addition, some distributions have instructions to not run the `.bashrc` instructions in a non-interactive bash invocation. Be sure to add the export command before the test for non-interactive use.