from shutil import copyfile

def do_not_block_websites():
    copyfile("/etc/hosts_backup_before_blocking" ,"/etc/hosts")

do_not_block_websites()

