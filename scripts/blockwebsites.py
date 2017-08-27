from shutil import copyfile

def block(website):
    return "127.0.0.1\t" + website.replace("\n", "") + "\n"


def block_websites():
    copyfile("/etc/hosts" ,"/etc/hosts_backup_before_blocking")
    with open("/etc/hosts", "a") as hostsFile:
        websitesFile = open("websites.txt", "r")
        websites = websitesFile.readlines()
        print(websites)
        websitesFile.close()
        for website in websites:
            hostsFile.write(block(website))
    hostsFile.close()


block_websites()

