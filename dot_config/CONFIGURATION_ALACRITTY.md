# Shell, Prompt, and Terminal Configuration

This repository provides instructions for configuring your Shell, Prompt, and Terminal on your system. Below are the prerequisites and steps to configure each component:

## Prerequisites

Before proceeding with the configuration, ensure you have a Nerd Font installed and enabled on your system.

## Alacritty

Before compiling Alacritty, you need to clone the source code:

```bash
git clone https://github.com/alacritty/alacritty.git
cd alacritty
```

Install the Rust compiler using rustup. If you already have it installed, make sure it's updated and set to use the stable version:

```bash
rustup override set stable
rustup update stable
```

Install the required dependencies:

```bash
sudo pacman -S cmake freetype2 fontconfig pkg-config make libxcb libxkbcommon python lsd bat
```

## Shell

Install Zsh using pacman:

```bash
pacman -S zsh
```

To set Zsh as your default shell, run the following command:

```bash
chsh -s zsh
```

## Install oh-my-zsh

# Oh-My-Zsh Installation

To install Oh-My-Zsh, you can use the following one-liner command:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

This command will download and execute the Oh-My-Zsh installation script, which will set up the framework for managing your Zsh configuration.

oh-my-zsh is a tool for managing Zsh configuration. Before setting up my Zsh configuration, make sure you have the zsh-antidote package installed. You can install it using a package manager like yay:

```bash
yay -S zsh-antidote
```

Alternatively, you can manually clone the antidote repository into your Zsh configuration directory:

```bash
# Run this from an interactive zsh terminal session:
git clone --depth=1 https://github.com/mattmc3/antidote.git ${ZDOTDIR:-~}/.antidote
```

To use my Zsh configuration, create the following symbolic links:

```bash
ln -s ~/.config/zsh/.zshrc ~/.zshrc
ln -s ~/.config/zsh/.zsh_plugins.zsh ~/.zsh_plugins.zsh
ln -s ~/.config/zsh/.zsh_plugins.txt ~/.zsh_plugins.txt
```

These symbolic links will link the configuration files in this repository to their appropriate locations in your home directory.

**Note:** If the .zshrc file has already been created by oh-my-zsh, delete it and create the symbolic link as indicated above.

## Shell Completions

If you haven't registered a directory for completions in your `~/.zshrc` yet, you can add one with the following command:

```bash
mkdir -p ${ZDOTDIR:-~}/.zsh_functions
echo 'fpath+=${ZDOTDIR:-~}/.zsh_functions' >> ${ZDOTDIR:-~}/.zshrc
```

## Install Prompt

### Prerequisites

Before proceeding with the installation of the Prompt, ensure you have a Nerd Font installed and enabled on your system.

To install the Prompt, you can use the following command:

```bash
curl -sS https://starship.rs/install.sh | sh
```

After the installation, add the following line to the end of your `~/.zshrc` file to initialize Starship when you start a new Zsh session:

```bash
eval "$(starship init zsh)"
```

That's it! With these configurations, your Shell, Prompt, and Terminal should be set up and ready to use. If you have any questions or issues, feel free to refer to the official documentation of each component for more information. Enjoy your terminal experience!
