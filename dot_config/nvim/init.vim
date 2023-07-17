set number
set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax enable
set showcmd
set ruler
set encoding=utf-8
set showmatch
set sw=2
set relativenumber
set laststatus=2
set noshowmode
set winblend=10


call plug#begin('~/.vim/plugged')


" Themes
Plug 'sainnhe/gruvbox-material'

" IDE
Plug 'easymotion/vim-easymotion'
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'

Plug 'ryanoasis/vim-devicons'

call plug#end()

" GRUVBOX config
set background=dark
let g:gruvbox_material_background = 'soft'
let g:gruvbox_material_better_performance = 1
colorscheme gruvbox-material

let NERDTreeQuitOnOpen=1
let mapleader=" "

" Change key
inoremap jj <Esc>

nmap <Leader>s <Plug>(easymotion-s2)

" NERDTREE Configuracion
let NERDTreeQuitOnOpen=1
nnoremap <silent> <F2> :NERDTreeFind<CR>
nnoremap <silent> <F3> :NERDTreeToggle<CR>

nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>
