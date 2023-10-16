import time

def countdown_timer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        
        if mins<10:
           timer=f'0{mins}: {secs}'
        else:
            timer=f'{mins}: {secs}'

        
        if secs<10:
            timer=f'{mins}: 0{secs}'
        else:
            timer=f'{mins}: {secs}'

        print(timer,end='\r')

        time.sleep(1)
        
        seconds -= 1

    print('time up')
seconds = input("Enter the time in seconds: ")
countdown_timer(int(seconds))