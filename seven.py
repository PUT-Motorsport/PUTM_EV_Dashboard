from graphics import *

class horz_segment:
    def __init__(self,x,y,w):
        self.step = w/6
        self.segment = Polygon(Point(x+self.step/2,y+self.step/2),Point(x+self.step,y+self.step),Point(x+self.step*4,y+self.step),
                    Point(x+self.step*4.5,y+self.step/2),Point(x+self.step*4,y),Point(x+self.step,y))

class vert_segment:
    def __init__(self,x,y,w):
        self.step = w/6
        self.segment = Polygon(Point(x+self.step/2,y+self.step/2),Point(x+self.step,y+self.step),Point(x+self.step,y+4*self.step),
                        Point(x+self.step/2,y+self.step*4.5),Point(x,y+self.step*4),Point(x,y+self.step))

class number:
    def __init__(self,x,y,w,win):
        self.segments = [horz_segment(x,y,w),horz_segment(x,y+w*4/6,w),horz_segment(x,y+8/6*w,w),vert_segment(x,y,w),
                        vert_segment(x+4/6*w,y,w),vert_segment(x+4/6*w,y+4/6*w,w),vert_segment(x,y+4/6*w,w)]
        for i in self.segments:
            i.segment.setFill("white")
        self.win = win
    def display_number(self,x):
        for i in self.segments:
            i.segment.undraw()
        if x==0:
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
        elif x==1:
            self.segments[4].segment.draw(self.win)
            self.segments[5].segment.draw(self.win)
        elif x==2:
            self.segments[0].segment.draw(self.win)
            self.segments[1].segment.draw(self.win)
            self.segments[2].segment.draw(self.win)
            self.segments[6].segment.draw(self.win)
            self.segments[4].segment.draw(self.win)
        elif x==3:
            self.segments[0].segment.draw(self.win)
            self.segments[1].segment.draw(self.win)
            self.segments[2].segment.draw(self.win)
            self.segments[4].segment.draw(self.win)
            self.segments[5].segment.draw(self.win)
        elif x==4:
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
        elif x==5:
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
        elif x==6:
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
        elif x==7:
            self.segments[4].segment.draw(self.win)
            self.segments[5].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
        elif x==8:
            for i in self.segments:
                i.segment.draw(win)
        elif x==9:
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
            self.segments[0].segment.draw(self.win)
                
