# import the pygame module, so you can use it
import math
import pygame
 
# define a main function
def main():
    bt="1 2 5 3 7 4 8"#input("input burst times:")
    bt=bt.split(' ')
    bt=[int(x) for x in bt]
    bt=[(i,bt[i]) for i in range(len(bt))]
    bt.sort(key=lambda x : x[1])
    bt_sum=sum([x[1] for x in bt])
    bt_pos=0
    for i in range(len(bt)):
        bt[i]=(bt[i][0],bt[i][1],bt_pos,bt_pos+bt[i][1])
        bt_pos+=bt[i][1]#math.floor(get_process_width(bt[i][1],bt_sum,700))
    print(bt)
    print(bt_sum)
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800,600))
     
     	
    screen.fill((200,230,200))
    
    # load font, prepare values
    font = pygame.font.Font(None, 16)
    text = "Fonty"
    size = font.size(text)

    # no AA, no transparency, normal

    pygame.draw.rect(screen,(200,200,200),(50,50,700,100))
    pygame.draw.rect(screen,(10,20,10),(50,50,700,100),3)
    for x in bt:
        start=math.floor(get_process_width(x[2],bt_sum,700))
        w=math.floor(get_process_width(x[1],bt_sum,700))
        pygame.draw.line(screen,(10,20,10),(50+start+w,50),(50+start+w,149),3)
        ren = font.render("P"+str(x[0]), 1, (0,0,0))
        screen.blit(ren, (50+start+w/2-ren.get_width()/2, 100-ren.get_rect().height/2))
        ren = font.render(str(x[2]), 1, (0,0,0))
        screen.blit(ren, (50+start-ren.get_width()/2, 150))
        ren = font.render(str(x[2]+x[1]), 1, (0,0,0))
        screen.blit(ren, (50+start+w-ren.get_width()/2, 150))


    pygame.draw.rect(screen,(10,20,10),(50,200,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(147,200,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(244,200,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(341,200,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(438,200,100,30),3)
    ren = font.render("Process", 1, (0,0,0))
    screen.blit(ren, (50+50-ren.get_width()/2, 210))
    ren = font.render("Burst Time", 1, (0,0,0))
    screen.blit(ren, (147+50-ren.get_width()/2, 210))
    ren = font.render("Waiting Time", 1, (0,0,0))
    screen.blit(ren, (244+50-ren.get_width()/2, 210))
    ren = font.render("Turnaround Time", 1, (0,0,0))
    screen.blit(ren, (341+50-ren.get_width()/2, 210))
    ren = font.render("Response Time", 1, (0,0,0))
    screen.blit(ren, (438+50-ren.get_width()/2, 210))

    for i in range(len(bt)):
        y=227+27*i
        pygame.draw.rect(screen,(10,20,10),(50,y,100,30),3)
        pygame.draw.rect(screen,(10,20,10),(147,y,100,30),3)
        pygame.draw.rect(screen,(10,20,10),(244,y,100,30),3)
        pygame.draw.rect(screen,(10,20,10),(341,y,100,30),3)
        pygame.draw.rect(screen,(10,20,10),(438,y,100,30),3)
        ren = font.render("P"+str(bt[i][0]), 1, (0,0,0))
        screen.blit(ren, (50+50-ren.get_width()/2, y+10))
        ren = font.render(str(bt[i][1]), 1, (0,0,0))
        screen.blit(ren, (147+50-ren.get_width()/2, y+10))
        ren = font.render(str(bt[i][2]), 1, (0,0,0))
        screen.blit(ren, (244+50-ren.get_width()/2, y+10))
        ren = font.render(str(bt[i][3]), 1, (0,0,0))
        screen.blit(ren, (341+50-ren.get_width()/2, y+10))
        ren = font.render(str(bt[i][2]), 1, (0,0,0))
        screen.blit(ren, (438+50-ren.get_width()/2, y+10))

    y=227+27*len(bt)
    pygame.draw.rect(screen,(10,20,10),(50,y,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(147,y,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(244,y,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(341,y,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(438,y,100,30),3)
    ren = font.render("Average", 1, (0,0,0))
    screen.blit(ren, (50+50-ren.get_width()/2, y+10))
    ren = font.render(str(round(sum([x[1] for x in bt])/len(bt),2)), 1, (0,0,0))
    screen.blit(ren, (147+50-ren.get_width()/2, y+10))
    ren = font.render(str(round(sum([x[2] for x in bt])/len(bt),2)), 1, (0,0,0))
    screen.blit(ren, (244+50-ren.get_width()/2, y+10))
    ren = font.render(str(round(sum([x[3] for x in bt])/len(bt),2)), 1, (0,0,0))
    screen.blit(ren, (341+50-ren.get_width()/2, y+10))
    ren = font.render(str(round(sum([x[2] for x in bt])/len(bt),2)), 1, (0,0,0))
    screen.blit(ren, (438+50-ren.get_width()/2, y+10))

    pygame.display.flip()

    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
def get_process_width(burst_time:int,total_time:int,total_width:int):
    return (burst_time/float(total_time))*total_width

def get_process_start():
    pass




# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()