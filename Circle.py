import math

def main():
    c = Circle(0,0,2)
    print(c.getXY(math.radians(60)))
    
    
class Circle:
    def __init__(self, centerX, centerY, radius):
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius

    def getXYCenterToRadius(self,theta):
        return (self.centerX + self.radius * math.cos(theta),
                self.centerY + self.radius * math.sin(theta))


if __name__ == "__main__":
    main()
