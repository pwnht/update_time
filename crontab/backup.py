#!/usr/bin/env python
from update_time import *
backup=update_time('backup',30)
backup.command="cd /&&tar -N "+backup.update_day+" --use-compress-program=pigz -cvpf /home/arch-backup.tgz --exclude-from=//home/pwnht/crontab/backup_blacklist.txt /"
backup.update_name()