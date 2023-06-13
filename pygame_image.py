import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_1=pg.transform.flip(bg_img,True,False)
    bg_img_2 = pg.image.load("ex01/fig/3.png")
    bg_img_2_1=pg.transform.flip(bg_img_2,True,False)
    bg_img_2_2=pg.transform.rotozoom(bg_img_2_1,10,1.0)
    bg_img_2_3=pg.transform.rotozoom(bg_img_2_1,5,1.0)
    haikei_list=[bg_img,bg_img_1]
    kyara_list=[bg_img_2_1,bg_img_2_3,bg_img_2_2,bg_img_2_3]
    tmr = 0
    y=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x=tmr%3200
        if tmr%10==0:
            y+=1
        screen.blit(bg_img,[-x,0])
        screen.blit(bg_img_1,[1600-x,0])
        screen.blit(bg_img,[3200-x,0])
        screen.blit(kyara_list[y%4],[300,200])
        pg.display.update()    
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()