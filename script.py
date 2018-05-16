import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [0,
              255,
              255]]
    areflect = [0.1,
                0.1,
                0.1]
    dreflect = [0.5,
                0.5,
                0.5]
    sreflect = [0.5,
                0.5,
                0.5]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 20

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
        i = 0
        while (i < len(commands)):
            if (commands[i][0] == "push"):
                stack.append([x[:] for x in systems[-1]])
                #print commands[i][0]
                #mdl.p_command_stack(commands[i][0])
            if (commands[i][0] == "pop"):
                stack.pop()
                #mdl.p_command_stack(commands[i][0])
            if (commands[i][0] == "save"):
                #mdl.p_command_save(commands[i])
            if (commands[i][0] == "display"):
                #mdl.p_command_show(commands[i])
            i = i + 1
    else:
        print "Parsing failed."
        return
