import copy
import random
# Consider using the modules imported above.



class Hat:
    def __init__(self,**kwargs):
        self.contents  = list()
        for (k,v) in kwargs.items():
           for i in range(int(v)) :
             self.contents.append(k)
    def draw(self,number):
        if len(self.contents) < int(number) :
            return self.contents
        
        new_draw =list()
        new_index = list()
        for i in range(int(number)):
            indexes = range(len(self.contents))
            ball = random.choice(indexes)
            while ball in new_index :
                ball = random.choice(indexes)
            
            new_draw.append(self.contents[ball])
            new_index.append(ball)
            del self.contents[ball]

        return new_draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
    accept = True
    for i in range(int(num_experiments)):
        new_hat = copy.deepcopy(hat)
        accept = True
        balls = new_hat.draw(int(num_balls_drawn))
        for (k,v) in expected_balls.items():
            if balls.count(k) < int(v) :
                accept = False
                break
        counter = counter + 1 if accept == True else counter 
    
    return counter/int(num_experiments)

