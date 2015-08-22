import time

def epoch_year():
    day = 0
    for i in range(0, 2016):
        if (i % 100 == 0) or (i % 400 == 0) or (i % 4 == 0):
            days = 366
            day = day + days
        else:
            days = 365
            day = day + days
    a = day - 365 + 167
    tot_sec = a * 24 * 60 * 60
    curr_time = time.time()
    diff = tot_sec - curr_time
    epoch = diff/(day*24*60*60)
    print "total days", a
    print "total sec", tot_sec
    print "curr_time", curr_time
    print "diff", diff
    print "epoch year", epoch

epoch_year()

