import datetime
import time

import unblock_websites
import block_websites

start_time = datetime.time(8 , 0 ,0 , 0)
end_time = datetime.time(18 , 0 ,0 , 0)
block = False

while True:
    time.sleep(10)
    currTime = datetime.datetime.now().time()
    if  (start_time < currTime < end_time):
        if block == True: continue
        block_websites.block_websites_func()
        block = True
    else:
        if  block == True:
            unblock_websites.do_not_block_websites()
            block = False





