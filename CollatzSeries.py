import simplegui

# global state

result = 1
iteration = 0
max_iterations = 27

# helper functions
def init(start):
    """Initializes n."""
    global n
    n = start
    print "Input is", n
    
def get_next(current):
    """???  Part of mystery computation."""
    global n 
    n = current
    #print "Input is", n
    if (n % 2 == 0):
        n = n /2
        return n
    else:
        n = n * 3 + 1
        return n
    

# timer callback

def update():
    """???  Part of mystery computation."""
    global iteration
    iteration += 1
    # Stop iterating after max_iterations
    if iteration >= max_iterations:
        timer.stop()
        print "Output is", n
    else:
        result = get_next(n)
        print result

# register event handlers

timer = simplegui.create_timer(1, update)

# start program
init(217)
timer.start()
#23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1

