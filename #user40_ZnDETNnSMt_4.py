# template for "Stopwatch: The Game"

# Import modules
import simplegui

# define global variables
interval = 100
position = [100, 100]
displaytime = "0:00.0"
currenttime = 0
times_stop_X = 0
times_stop_Y = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global displaytime    
    A = t / 600
    BC = t % 600
    BC = BC / 10
    D = (t % 600) % 10
    if len(str(BC)) < 2:
        displaytime = str(A) + ":0" + str(BC) + "." + str(D)
    else:
        displaytime = str(A) + ":" + str(BC) + "." + str(D)
    return displaytime
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global currenttime, times_stop_X, times_stop_Y
    if currenttime % 20 == 0:
        times_stop_X += 1
    times_stop_Y += 1
    timer.stop()

def reset():
    global message, displaytime, currenttime, times_stop_X, times_stop_Y
    displaytime = "0:00.0"
    currenttime = 0
    times_stop_X = 0
    times_stop_Y = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global message, currenttime, displaytime
    currenttime += 1
    displaytime = format(currenttime)
    
# define draw handler
def draw(canvas):
    canvas.draw_text(displaytime, position, 36, "White")
    canvas.draw_text(str(times_stop_X)+ "/" + str(times_stop_Y), [230, 50], 25, "White")
    canvas.draw_text("Every 2 secends need to stop", [20,45], 15, "White")

    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)

# register event handlers
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw)
btnStart = frame.add_button('Start', start, 100)
btnStop = frame.add_button('Stop', stop, 100)
btnReset = frame.add_button('Reset', reset, 100)

# start frame
frame.start()

# Please remember to review the grading rubric
