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
LEFT = 'LEFT'
RIGHT = 'RIGHT'

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    vel_x = random.randrange(2,5)
    vel_y = random.randrange(1,4)
    
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction.upper() == LEFT:
        ball_vel = [-vel_x, -vel_y]
    else:
        ball_vel = [vel_x, -vel_y]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

    paddle1_pos = (HEIGHT / 2) - (PAD_HEIGHT / 2)
    paddle2_pos = (HEIGHT / 2) - (PAD_HEIGHT / 2)
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0

    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    if touch_right():
        score1 += 1
        spawn_ball(LEFT)
    elif touch_left():
        score2 += 1
        spawn_ball(RIGHT)
    
    # update ball
    if touch_left() or touch_right():
        ball_vel[0] = -ball_vel[0]

    if touch_top() or touch_bottom():
        ball_vel[1] = -ball_vel[1]
        
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'white', 'white')
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel >= 0 and paddle1_pos + PAD_HEIGHT + paddle1_vel <= HEIGHT):
        paddle1_pos += paddle1_vel
        
    if (paddle2_pos + paddle2_vel >= 0 and paddle2_pos + PAD_HEIGHT + paddle2_vel <= HEIGHT):
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line([PAD_WIDTH / 2, paddle1_pos], [PAD_WIDTH / 2, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "white")
    canvas.draw_line([WIDTH - (PAD_WIDTH / 2), paddle2_pos], [WIDTH - (PAD_WIDTH / 2), paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "white")
    
    # determine whether paddle and ball collide    
    if touch_left() and ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
        ball_vel[0] = - ball_vel[0]
        if ball_vel[0] > 0:
            ball_vel[0] += 1
        else:
            ball_vel[0] -= 1
    
    elif touch_right() and ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
        ball_vel[0] = - ball_vel[0]
        if ball_vel[0] > 0:
            ball_vel[0] += 1
        else:
            ball_vel[0] -= 1
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH/4, HEIGHT /4), 60, 'white')
    canvas.draw_text(str(score2), (WIDTH - WIDTH/4, HEIGHT /4), 60, 'white')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel += -2
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += 2

    if key == simplegui.KEY_MAP['up']:
        paddle2_vel += -2
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += 2
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0

    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    

def touch_right():
    return ball_pos[0] + ball_vel[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH
    
def touch_left():
    return ball_pos[0] + ball_vel[0] - BALL_RADIUS <= PAD_WIDTH
    
def touch_bottom():
    return ball_pos[1] + ball_vel[1] + BALL_RADIUS >= HEIGHT
    
def touch_top():
    return ball_pos[1] + ball_vel[1] - BALL_RADIUS <= 0
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
