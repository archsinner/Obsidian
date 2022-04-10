## 4.3. Adding the LFS User

When logged in as user `root`, making a single mistake can damage or destroy a system. Therefore, the packages in the next two chapters are built as an unprivileged user. You could use your own user name, but to make it easier to set up a clean working environment, create a new user called `lfs` as a member of a new group (also named `lfs`) and use this user during the installation process. As `root`, issue the following commands to add the new user:

groupadd lfs
useradd -s /bin/bash -g lfs -m -k /dev/null lfs

**The meaning of the command line options:**

_`-s /bin/bash`_

This makes **bash** the default shell for user `lfs`.

_`-g lfs`_

This option adds user `lfs` to group `lfs`.

_`-m`_

This creates a home directory for `lfs`.

_`-k /dev/null`_

This parameter prevents possible copying of files from a skeleton directory (default is `/etc/skel`) by changing the input location to the special null device.

_`lfs`_

This is the actual name for the created user.

To log in as `lfs` (as opposed to switching to user `lfs` when logged in as `root`, which does not require the `lfs` user to have a password), give `lfs` a password:

passwd lfs

Grant `lfs` full access to all directories under `$LFS` by making `lfs` the directory owner:

chown -v lfs $LFS/{usr{,/*},lib,var,etc,bin,sbin,tools}
case $(uname -m) in
  x86_64) chown -v lfs $LFS/lib64 ;;
esac

If a separate working directory was created as suggested, give user `lfs` ownership of this directory:

chown -v lfs $LFS/sources

### Note

In some host systems, the following command does not complete properly and suspends the login to the lfs user to the background. If the prompt "lfs:~$" does not appear immediately, entering the **fg** command will fix the issue.

Next, login as user `lfs`. This can be done via a virtual console, through a display manager, or with the following substitute/switch user command:

su - lfs

The “_`-`_” instructs **su** to start a login shell as opposed to a non-login shell. The difference between these two types of shells can be found in detail in `bash(1)` and **info bash**.