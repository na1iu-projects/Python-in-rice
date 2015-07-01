# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2 , HEIGHT / 2]
ball_vel = [0, 0]
paddle1_vel = 0  
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2 , HEIGHT / 2]
    vel_X = random.randrange(2, 5)
    vel_Y = random.randrange(1, 4)
    if direction == True:
        ball_vel = [vel_X, - vel_Y]
    elif direction == False:
        ball_vel = [- vel_X, - vel_Y]  
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2 # these are ints
    score1, score2 = 0, 0
    paddle1_pos = [PAD_WIDTH / 2, HEIGHT / 2]
    paddle2_pos = [WIDTH - PAD_WIDTH / 2, HEIGHT / 2]
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
       
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
        spawn_ball(RIGHT)
    elif ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
        spawn_ball(LEFT)
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] < HALF_PAD_HEIGHT:
        paddle1_pos[1] = HALF_PAD_HEIGHT
        paddle1_vel = 0
    elif paddle1_pos[1] > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
        paddle1_vel = 0
    if paddle2_pos[1] < HALF_PAD_HEIGHT:
        paddle2_pos[1] = HALF_PAD_HEIGHT
        paddle2_vel = 0
    elif paddle2_pos[1] > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
        paddle2_vel = 0
    
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    # draw paddles
    canvas.draw_line([paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT],[paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT], 8,"White")
    canvas.draw_line([paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT],[paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT], 8,"White")
    
    # determine whether paddle and ball collide    
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if (paddle1_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT):
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
    
    if ball_pos[0] >= (WIDTH - PAD_WIDTH) - BALL_RADIUS:
        if (paddle2_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT):
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
        
    # draw scores
    canvas.draw_text(str(score1), (450, 50), 36, "White")
    canvas.draw_text(str(score2), (150, 50), 36, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5  
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc  
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc    
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc  
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()
