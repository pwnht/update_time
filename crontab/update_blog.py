#!/usr/bin/env python
from update_time import *
command="git config --global user.name 'User'&&"
command+="git config --global user.email 'e-mail'&&"
command+="cd /home/pwnht/git/&&"
command+="git remote set-url origin git@github.com:user/user.git&&"
command+="git add .&&git commit -m 'update'&&git push&&"
command+="hexo clean&&hexo g&&hexo d"
blog=update_time('blog',7,command)
blog.update_name()
