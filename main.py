from classses import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES, pygame.SRCALPHA)
        self.clock = pygame.Clock()
        
        self.setup()
    
    def setup(self):    
        self.ball = V2(1,1)
        self.time = 0
        self.time_speed = 0.2
        
        self.chains = []
        i = 0
        while (i < 2*pi):
            self.chains.append(Chain(15, 300, 2, 8, V2(HW + 500*cos(i), HH + 500*sin(i))))
            i += (2*pi)/50
        
    def update(self):
        # ball
        self.ball.x = 2*perlin_noise(V2(self.time, 0), V2(80,60)) * W - HW
        self.ball.y = 2*perlin_noise(V2(0, self.time), V2(80,60)) * H - HH
        
        self.time += self.time_speed * self.dt
        self.time %= 1000
        pygame.draw.circle(self.screen, 'green', self.ball, 30)
        
        # tentacles
        for chain in self.chains:
            # chain.update(self.ball)
            chain.update(pygame.mouse.get_pos())
            chain.draw(self.screen) 

    def run(self):
        self.running = True
        while self.running:
            self.dt = 200*self.clock.tick()/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
                    
            self.screen.fill(BACKGROUND)
            self.update()
            pygame.display.set_caption(f'FPS: {self.clock.get_fps()}')
            pygame.display.flip()
            
            
Game().run()
            