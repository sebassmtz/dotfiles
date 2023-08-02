# Prerequisites and Build

Before proceeding with the configuration and setup of Alacritty, please ensure you have the necessary prerequisites installed on your system. The build process requires a Nerd Font, Rust compiler, and other dependencies. Follow the steps below to set up Alacritty:

## Prerequisites

1. Install a Nerd Font:
   Nerd Fonts are required to display custom icons and symbols in Alacritty. Install a Nerd Font of your choice on your system. You can find Nerd Fonts at: [https://www.nerdfonts.com/](https://www.nerdfonts.com/)

2. Install Rust Compiler:

   ```shell
   sudo pacman -S rust
   ```

## Alacritty Installation

1. Clone the Alacritty Source Code:

   ```shell
   git clone https://github.com/alacritty/alacritty.git
   cd alacritty
   ```

2. Install Dependencies:

   On Linux, Windows, and BSD systems, install the required dependencies:

   ```shell
   sudo pacman -S cmake freetype2 fontconfig pkg-config make libxcb libxkbcommon python lsd bat
   ```

3. Build Alacritty:

   Run the following command inside the Alacritty repository:

   ```shell
   cargo build --release
   ```

## Post Build Setup

After successfully building Alacritty, there are some extra configurations you may want to perform:

### Desktop Entry (Linux/BSD):

To add Alacritty to system menus on Linux or BSD distributions, you can create a desktop entry:

```shell
sudo cp target/release/alacritty /usr/local/bin # or anywhere else in $PATH
sudo cp extra/logo/alacritty-term.svg /usr/share/pixmaps/Alacritty.svg
sudo desktop-file-install extra/linux/Alacritty.desktop
sudo update-desktop-database
```

For more detailed installation instructions, you can refer to the [INSTALL.md](https://github.com/alacritty/alacritty/blob/master/INSTALL.md) file in the Alacritty repository.

Feel free to explore and customize Alacritty according to your preferences. Enjoy using Alacritty as your terminal emulator! 😊
