from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x0 = int(x0)
    x1 = int(x1)
    y0 = int(y0)
    y1 = int(y1)
    #vertical line
    if x0 == x1:
        if y1 < y0:
            y1, y0 = y0, y1
        while y0 <= y1:
            plot(screen, color, x0, y0)
            y0 += 1
    #horizontal line
    elif y0 == y1:
        if x1 < x0:
            x0, x1 = x1, x0
        while x0 <= x1:
            plot(screen, color, x0, y0)
            x0 += 1
    else:
        # Octant 1 & 5
        if x1 < x0:
            x0, x1, y0, y1 = x1, x0, y1, y0
        A = y1 - y0
        B = x0 - x1
        m = (y1 - y0) / (x1 - x0)
        if (m <= 1 and m >= 0):
            d = 2 * A + B
            A = 2 * A
            B = 2 * B
            while (x0 <= x1):
                plot(screen , color, x0, y0)
                if d >+ 0:
                    y0 += 1
                    d = d + B
                x0 += 1
                d = d + A
        # Octant 2 & 6
        elif (m > 1):
            d = A + 2 * B
            A = 2 * A
            B = 2 * B
            while (y0 <= y1):
                plot(screen, color, x0, y0)
                if (d <+ 0):
                    x0 += 1
                    d += A
                y0 += 1
                d += B
        #Octant 4 & 8
        elif (m <= 0 and m >= - 1):
            d = 2 * A + B
            A = 2 * A
            B = 2 * B
            while (x0 <= x1):
                plot(screen , color, x0, y0)
                if d <+ 0:
                    y0 -= 1
                    d = d - B
                x0 += 1
                d = d + A
        #Octant 3 & 7
        elif (m < - 1):
            d = A - 2 * B
            A = 2 * A
            B = 2 * B
            while (y0 >= y1):
                # print("here")
                plot(screen, color, x0, y0)
                if (d > 0):
                    x0 += 1
                    d = d + A
                y0 -= 1
                d = d - B
