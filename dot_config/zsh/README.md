# ZSH Config

This repository contains my Zsh configuration, which I use to customize my Zsh shell. It includes several plugins and settings that enhance my terminal experience.

## Dependencies

Before setting up my Zsh configuration, please make sure you have the `zsh-antidote` package installed. You can install it using a package manager like `yay`:

```bash
yay -S zsh-antidote
```

Alternatively, you can manually clone the `antidote` repository into your Zsh configuration directory:

```bash
# Run this from an interactive zsh terminal session:
git clone --depth=1 https://github.com/mattmc3/antidote.git ${ZDOTDIR:-~}/.antidote
```

## Symbolic links

To use my Zsh configuration, create the following symbolic links:

```bash
ln -s ~/.config/zsh/.zshrc ~/.zshrc
ln -s ~/.config/zsh/.zsh_plugins.zsh ~/.zsh_plugins.zsh
ln -s ~/.config/zsh/.zsh_plugins.txt ~/.zsh_plugins.txt
```

These symbolic links will link the configuration files in this repository to their appropriate locations in your home directory.

Please note that you may need to adjust the paths based on your setup.

Feel free to explore and customize the configuration according to your preferences. If you have any suggestions or improvements, feel free to contribute!

Enjoy using my Zsh configuration! 😊
