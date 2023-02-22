class Valuable:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
        
class SafeDepositBox:
    def __init__(self, size):
        self.size = size
        self.valuables = []
        
    def add(self, valuable):
        if self.available_space() >= valuable.volume:
            self.valuables.append(valuable)
            return True
        return False
    
    def remove(self, valuable):
        if valuable in self.valuables:
            self.valuables.remove(valuable)
            return True
        return False
    
    def available_space(self):
        used_space = sum([v.volume for v in self.valuables])
        return self.size - used_space
