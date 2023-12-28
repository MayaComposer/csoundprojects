import ctcsound
import PySimpleGUI as sg 
import keyboard


#initilise stuff

# Function to increase the variable
def increase_variable(var):
    var += 1
    return var

current_cue = 0

spacebar_pressed = False


#gui
layout = [  [sg.Text('Cue')],
            [sg.Text(size=(2,2),
                   key='OUT', auto_size_text = True)]  ]
            
layout = [[sg.Sizer(0,500), sg.Column([[sg.Sizer(500,0)]] + layout, element_justification='c', pad=(0,0))]]

window = sg.Window('Window Title', layout, margins=(0,0))

#start csound
cs = ctcsound.Csound() # create an instance of Csound
cs.compileCsd("sound.csd")
cs.start()             # When compiling from strings, this call is necessary before doing any performing

t = ctcsound.CsoundPerformanceThread(cs.csound()) # Create a new CsoundPerformanceThread, passing in the Csound object
t.play()              # starts the thread, which is now running separately from the main thread. This 
                      # call is asynchronous and will immediately return back here to continue code
                      # execution.



#event loop when application runs
while True:
    #not entirely sure what this means tbh
    event, values = window.read(timeout=100)

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break


    #to next cue. This should probably also send to Csound
    if keyboard.is_pressed("space") and not spacebar_pressed:
        current_cue = increase_variable(current_cue)
        spacebar_pressed = True
    elif not keyboard.is_pressed("space") and spacebar_pressed:
        spacebar_pressed = False
            

    #update GUI
    window['OUT'].update(current_cue)



# Finish up by removing from the screen
window.close()
del cs
