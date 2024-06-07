class Animal:
    def __init__(self):
        self.num_eyes=2
    def breathe(self):
        print("Inhale ,Exhalle.")
class fish(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("doing this underwater")
    def swim(self):
        print("moving in water .")
ash=fish()
ash.swim()
ash.breathe
print(ash.num_eyes)