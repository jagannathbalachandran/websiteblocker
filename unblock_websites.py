from shutil import copyfile

def do_not_block_websites():
    print("unblocking websites")
    copyfile("/etc/hosts_backup_before_blocking" ,"/etc/hosts")


