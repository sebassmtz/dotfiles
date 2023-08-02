# My ZSH Configuration

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![GitHub stars](https://img.shields.io/github/stars/sebastian01973/dotfiles.svg)
![GitHub forks](https://img.shields.io/github/forks/sebastian01973/dotfiles.svg)

This repository contains my ZSH configuration setup, including the installation of Zsh, Oh-My-Zsh, and additional customizations.

## Installation

### 1. Install Zsh using pacman:

```shell
pacman -S zsh
```

### 2. Set Zsh as your default shell:

```shell
chsh -s zsh
#or 
chsh -s  /usr/bin/zsh
```

### 3. Install Oh-My-Zsh:

To install Oh-My-Zsh, you can use the following one-liner command:

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Oh-My-Zsh is a powerful tool for managing Zsh configurations.

### 4. Install zsh-antidote:

Before setting up my Zsh configuration, make sure you have the `zsh-antidote` package installed. You can install it using a package manager like `yay`:

```shell
yay -S zsh-antidote
```

### 5. Symbolic links:

To use my Zsh configuration, create the following symbolic links:

```shell
ln -s ~/.config/zsh/.zshrc ~/.zshrc
ln -s ~/.config/zsh/.zsh_plugins.zsh ~/.zsh_plugins.zsh
ln -s ~/.config/zsh/.zsh_plugins.txt ~/.zsh_plugins.txt
```

These symbolic links will link the configuration files in this repository to their appropriate locations in your home directory.

### 6. Install Starship Prompt:

#### Prerequisites:

Before proceeding with the installation of the Starship Prompt, ensure you have a Nerd Font installed and enabled on your system.

#### Installation:

To install the Starship Prompt, you can use the following command:

```shell
curl -sS https://starship.rs/install.sh | sh
```

Please note that you may need to adjust the paths based on your setup.

## Customization

Feel free to explore and customize the configuration according to your preferences. You can modify the `.zshrc` file and other configuration files to suit your needs.

## Contributing

If you have any suggestions, improvements, or new features to add to this Zsh configuration, feel free to contribute! Pull requests are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- Email - sebastian0197333@gmail.com
- GitHub - [Your GitHub Username](https://github.com/sebastian01973)

Enjoy using my Zsh configuration! 😊
