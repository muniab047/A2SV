class Robot:

    def __init__(self, width: int, height: int):
        self.direction='East'
        self.position=[0,0]
        self.width=width-1
        self.height=height-1

        

    def step(self, num: int) -> None:
        step=0
        num=num%(2*(self.width+self.height))
        num += (2*(self.width+self.height))
        print(num)
        while(num>0):
            x,y=self.position
            if(x<self.width and y==0):
                step=min(num,self.width-x)
                self.position[0]+=step
                self.direction="East"
            elif(x==self.width and y<self.height):
                step=min(num,self.height-y)
                self.position[1]+=step
                self.direction="North"
            
            elif(x<=self.width and y==self.height and x!=0):
                step=min(num,x)
                self.position[0]-=step
                self.direction="West"

            elif(x==0 and y<=self.height and y!=0):
                step=min(num,y)
                self.position[1]-=step
                self.direction="South"

            num-=step

    def getPos(self) -> List[int]:
        return self.position
        

    def getDir(self) -> str:
        return self.direction
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()