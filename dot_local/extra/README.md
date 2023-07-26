**README.md - Installation Instructions**

### Package Installation

To install the packages available in this repository using `sudo pacman -U`, follow the steps below:

1. First, make sure you have the `pacman` package manager installed on your system. If you don't have it installed, you can install it by running the following command:

   ```bash
   sudo pacman -S pacman
   ```

2. Clone this repository to your local machine (if you haven't done so already):

   ```bash
   git clone https://github.com/Sebastian01973/dotfiles.git
   ```

3. Navigate to the folder containing the additional packages:

   ```bash
   cd dotfiles/dot_local/extra
   ```

4. Next, use `sudo pacman -U` to install the packages you desire. Make sure to replace `PACKAGE_NAME` with the actual name of the package you wish to install:

   ```bash
   sudo pacman -U fonts.pkg.tar.zst gtk-theme-arc.pkg.tar.zst icons-arc.pkg.tar.zst
   ```

   For example, if you want to install the packages `fonts.pkg.tar.zst`, `gtk-theme-arc.pkg.tar.zst`, and `icons-arc.pkg.tar.zst`, run the following command:

   ```bash
   sudo pacman -U fonts.pkg.tar.zst gtk-theme-arc.pkg.tar.zst icons-arc.pkg.tar.zst
   ```
5. Update fonts.
    ```bash
   sudo fc-cache -f -v
   ```

### Contribution

If you wish to contribute to this repository, feel free to do so through pull requests. Your contributions are welcome.
