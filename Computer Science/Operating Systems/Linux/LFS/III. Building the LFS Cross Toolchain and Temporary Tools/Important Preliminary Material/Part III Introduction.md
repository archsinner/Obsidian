# Part III. Building the LFS Cross Toolchain and Temporary Tools

## Important Preliminary Material

## Introduction

This part is divided into three stages: first building a cross compiler and its associated libraries; second, use this cross toolchain to build several utilities in a way that isolates them from the host distribution; third, enter the chroot environment, which further improves host isolation, and build the remaining tools needed to build the final system.

### Important

With this part begins the real work of building a new system. It requires much care in ensuring that the instructions are followed exactly as the book shows them. You should try to understand what they do, and whatever your eagerness to finish your build, you should refrain from blindly type them as shown, but rather read documentation when there is something you do not understand. Also, keep track of your typing and of the output of commands, by sending them to a file, using the **tee** utility. This allows for better diagnosing if something gets wrong.

The next section gives a technical introduction to the build process, while the following one contains **very important** general instructions.