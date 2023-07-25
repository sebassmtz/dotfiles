
# Neovim Configuration

## Installation

1. Install Neovim using the package manager of your operating system:

   - **On Arch Linux-based systems (e.g., Manjaro)**:
     ```
     sudo pacman -S neovim
     ```

   - **On other Unix/Linux systems, follow the instructions for your specific system**.

2. Install the plugin manager "vim-plug". Open a terminal and run the following command:

   ```
   sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
          https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
   ```

## Plugin Configuration

1. Open Neovim from the terminal:

   ```
   nvim
   ```

2. Once inside Neovim, execute the following command to install all the plugins specified in your configuration file:

   ```
   :PlugInstall
   ```

   This will download and install all the plugins defined in your configuration file.

3. Done! You should now have your plugins installed and working in Neovim.

## Customization

You can customize Neovim according to your preferences by editing the configuration file. The Neovim configuration file can be found at the following path:

```
~/.config/nvim/init.vim
```

You can add new plugins, adjust the appearance, and set keyboard shortcuts in this file. Experiment and find the configuration that best suits your needs!

## Additional Resources

- Official Neovim documentation: [https://neovim.io/doc/user/](https://neovim.io/doc/user/)
- vim-plug documentation: [https://github.com/junegunn/vim-plug](https://github.com/junegunn/vim-plug)

Enjoy your experience with Neovim and make the most of its potential! If you have any questions or issues, feel free to seek help from the Neovim community or consult the official documentation. Happy coding!

