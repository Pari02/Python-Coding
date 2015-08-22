# template for "Stopwatch: The Game"

import simplegui

# define global variables
sec = 0
sec_string = ""
game = 0
score = 0

# define helper function format that converts time 
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global sec
    global sec_string
    sec = int(t)
    A = 0
    B = 0 
    C = 0
    if (sec == 0):
        sec_string = "0" + ":" + "00" + "." + "0"
    else:
        A = sec / 600
        B = (sec % 600) / 10
        C = (sec % 600) % 10
        if B < 10:
            sec_string = str(A) + ":" + "0" + str(B) + "." + str(C)
        else:
            sec_string = str(A) + ":" + str(B) + "." + str(C)
    #print sec_string 
    return sec_string

# define a helper function to calculate and increment the game score
def game_score(val, scor):
    global game, score
    game = val
    if val == 0:
        score_str = "0" + "/" + "0"
    else:
        score_str = str(game) + "/" + str(score)
    return score_str
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    format(sec)
  
def stop():
    global sec, game, score
    timer.stop()
    if ((sec % 600) % 10) == 0:
        game += 1
        score += 1
        game_score(game, score)
    else:
        game += 1
        game_score(game, score)
    format(sec)

def reset():
    global sec
    timer.stop()
    sec = 0
    format(sec)
    
# define event handler for timer with 0.1 sec interval
def tick():
    global sec
    sec += 1
    format(sec)

# define draw handler
def draw(canvas):
    canvas.draw_text(format(sec), [150,150], 20, 'Yellow')
    canvas.draw_text(game_score(game, score), [260, 30], 20, 'Red')
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)
frame.set_canvas_background('Blue')

# register event handlers
frame.set_draw_handler(draw)
frame.add_button('Start', start)
frame.add_button('Stop', stop)
frame.add_button('Reset', reset)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()