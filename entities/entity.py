from abc import abstractmethod, ABC

class entity(ABC):
    
    def __init__(self,image):
        
        self.image=image
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def draw(self):
        pass


    
        
        