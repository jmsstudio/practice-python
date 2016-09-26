import simplegui

counter = 0

def format(t):
    minute = str(counter/600)
    second = str(counter%6000)
    
    show_sec = "00"
    show_dec = "0"
    
    if (int(second) >= 100):
        second = str(int(second)%600)

        show_sec = second[0:2]
        show_dec = second[-1]

    elif (int(second) >= 10):
        show_sec = "0" + second[0]
        show_dec = second[-1]
    else:
        show_sec = "00"
        show_dec = second[-1]
        
    return minute + ":" + show_sec + "." + show_dec
    
def handle_start():
    timer.start()

def handle_stop():
    timer.stop()

def handle_reset():
    global counter
    
    timer.stop()
    counter = 0

def tick():
    global counter
    counter += 1

def draw(canvas):
    global counter
    canvas.draw_text(format(counter), [150,100], 30, 'white')
    
frame = simplegui.create_frame("Stopwatch", 300, 200)

frame.add_button("start", handle_start, 100)
frame.add_button("stop", handle_stop, 100)
frame.add_button("reset", handle_reset, 100)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)


frame.start()
