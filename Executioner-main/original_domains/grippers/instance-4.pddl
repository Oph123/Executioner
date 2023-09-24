(define (problem gripper-7-8-12)
(:domain gripper-strips)
(:objects robot1 robot2 robot3 robot4 robot5 robot6 robot7 - robot
rgripper1 lgripper1 rgripper2 lgripper2 rgripper3 lgripper3 rgripper4 lgripper4 rgripper5 lgripper5 rgripper6 lgripper6 rgripper7 lgripper7 - gripper
room1 room2 room3 room4 room5 room6 room7 room8 - room
ball1 ball2 ball3 ball4 ball5 ball6 ball7 ball8 ball9 ball10 ball11 ball12 - stuff)
(:init
(at-robby robot1 room2)
(free robot1 rgripper1)
(free robot1 lgripper1)
(at-robby robot2 room6)
(free robot2 rgripper2)
(free robot2 lgripper2)
(at-robby robot3 room7)
(free robot3 rgripper3)
(free robot3 lgripper3)
(at-robby robot4 room7)
(free robot4 rgripper4)
(free robot4 lgripper4)
(at-robby robot5 room2)
(free robot5 rgripper5)
(free robot5 lgripper5)
(at-robby robot6 room6)
(free robot6 rgripper6)
(free robot6 lgripper6)
(at-robby robot7 room1)
(free robot7 rgripper7)
(free robot7 lgripper7)
(at ball1 room5)
(at ball2 room4)
(at ball3 room4)
(at ball4 room2)
(at ball5 room3)
(at ball6 room6)
(at ball7 room3)
(at ball8 room2)
(at ball9 room2)
(at ball10 room7)
(at ball11 room7)
(at ball12 room4)
)
(:goal
(and
(at ball1 room3)
(at ball2 room2)
(at ball3 room1)
(at ball4 room1)
(at ball5 room2)
(at ball6 room7)
(at ball7 room7)
(at ball8 room4)
(at ball9 room5)
(at ball10 room5)
(at ball11 room5)
(at ball12 room7)
)
)
)
