## 2.5. Creating a File System on the Partition

Now that a blank partition has been set up, the file system can be created. LFS can use any file system recognized by the Linux kernel, but the most common types are ext3 and ext4. The choice of file system can be complex and depends on the characteristics of the files and the size of the partition. For example:

ext2

is suitable for small partitions that are updated infrequently such as /boot.

ext3

is an upgrade to ext2 that includes a journal to help recover the partition's status in the case of an unclean shutdown. It is commonly used as a general purpose file system.

ext4

is the latest version of the ext file system family of partition types. It provides several new capabilities including nano-second timestamps, creation and use of very large files (16 TB), and speed improvements.

Other file systems, including FAT32, NTFS, ReiserFS, JFS, and XFS are useful for specialized purposes. More information about these file systems can be found at [http://en.wikipedia.org/wiki/Comparison_of_file_systems](http://en.wikipedia.org/wiki/Comparison_of_file_systems).

LFS assumes that the root file system (/) is of type ext4. To create an `ext4` file system on the LFS partition, run the following:

mkfs -v -t ext4 /dev/_`<xxx>`_

Replace _`<xxx>`_ with the name of the LFS partition.

If you are using an existing `swap` partition, there is no need to format it. If a new `swap` partition was created, it will need to be initialized with this command:

mkswap /dev/_`<yyy>`_

Replace _`<yyy>`_ with the name of the `swap` partition.