from settings import *
    
class Chain:
    def __init__(self, num_of_segments = 10, total_length = 150, start_width = 2, end_width = 10, base = V2(HW,H)):
        
        self.base = base
        self.segments = [Segment(total_length/num_of_segments, start_width)]
        for i in range(1,num_of_segments):
            self.segments.insert(0, Segment(total_length/num_of_segments, int(end_width*(i/num_of_segments) + start_width)))
            
    def draw(self,screen):
        for segment in self.segments:
            segment.draw(screen)
    
    def update(self, target):
        self.segments[-1].point_to_target(target)
        self.segments[-1].update()
        for i in range(len(self.segments)-2, -1, -1):
            self.segments[i].point_to_target(self.segments[i+1].a)
            self.segments[i].update()
            
        self.segments[0].set_A(V2(self.base))
        for i in range(1, len(self.segments)):
            self.segments[i].set_A(self.segments[i-1].b)
    
class Segment:
    def __init__(self, length, line_weight=10):
        
        self.a = V2(HW,HH)

        self.length = length
        self.angle = 0
        self.line_weight = line_weight
        
    def draw(self,screen):
        pygame.draw.line(screen, ACCENT, self.a, self.b, max(1, self.line_weight))
        
    def point_to_target(self, target):
        t_vec = V2(target) - self.a + V2(1,1)       # (1,1) grace for when target is the same as self.a
        self.angle = -(t_vec.angle_to(V2(1,0))) 
        t_vec.scale_to_length(self.length)
        t_vec = -t_vec
        self.a = V2(target) + t_vec
        
    def set_A(self, pos):
        self.a = V2(pos)
        self.update()
    
    def update(self):
        dx = self.length * cos(radians(self.angle))
        dy = self.length * sin(radians(self.angle))
        self.b = self.a + V2(dx, dy)
        


