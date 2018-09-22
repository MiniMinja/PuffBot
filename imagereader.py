import pyautogui
import time
import handler
class ImageReader:

    def tick(self):
        region = (1, 1, 3839, 1799)
        pink = (255 , 204 , 225)
        #mario = (0, 110, 0)
        pikachu = (254, 221, 74)
        yrange = range(region[1], region[3] + 1, 10)
        xrange = range(region[0], region[2] + 1, 10)
        while not handler.stop_flag:
            #print('Screenshot')
            img = pyautogui.screenshot(region=region)
            self.read_screen(pink, pikachu, xrange ,yrange)
            #mx, my = pyautogui.position() #71, 131, 1738, 1097
            #print('x: {} y: {}'.format(x, y))
            #print('x: {} y: {}'.format(mx, my))
            #print(pyautogui.pixel(mx, my))
            #time.sleep(1.0 / 100.0)
            handler.stop_flag = True

    def read_screen(self, jp_color, pik_color, xrange, yrange):
        jp_coors = [0, 0]
        pik_coors = [0, 0]
        jp_count = 0
        pik_count = 0
        #mario_coors = [-1, -1, -1, -1]
        for i in yrange:
            for j in xrange:
                px = pyautogui.pixel(j, i)
                if px == jp_color:
                    self.update_locs(jp_coors, i, j)
                    jp_count+=1
                if px == pik_color:
                    self.update_locs(pik_coors, i , j)
                    pik_count += 1
        if jp_count == 0 :
            jp_count += 1
        if pik_count == 0:
            pik_count += 1
        jp_coors[0] /= jp_count
        jp_coors[1] /= jp_count
        pik_coors[0] /= pik_count
        pik_coors[1] /= pik_count
        if jp_coors[0] == 0:
            handler.jp.stop_moving()
            handler.jp.move_down()
        else:
            handler.jp.stop_moving_down()
            if jp_coors[0] - pik_coors[0] > 100:
                handler.jp.short_jump()
            elif jp_coors[1] - pik_coors[1] < -20:
                handler.jp.stop_moving_left()
                handler.jp.move_right()
            elif jp_coors[1] - pik_coors[1] > 20:
                handler.jp.stop_moving_right()
                handler.jp.move_left()

        #print(jp_coors[1] - pik_coors[1])
        print(jp_coors)
        print(pik_coors)

    def read_screen(self, img, jp_color, pik_color, xrange, yrange):
        jp_coors = [0, 0]
        pik_coors = [0, 0]
        jp_count = 0
        pik_count = 0
        #mario_coors = [-1, -1, -1, -1]
        for i in yrange:
            for j in xrange:
                px = img.getpixel((j, i))
                if px == jp_color:
                    self.update_locs(jp_coors, i, j)
                    jp_count+=1
                if px == pik_color:
                    self.update_locs(pik_coors, i , j)
                    pik_count += 1
        if jp_count == 0 :
            jp_count += 1
        if pik_count == 0:
            pik_count += 1
        jp_coors[0] /= jp_count
        jp_coors[1] /= jp_count
        pik_coors[0] /= pik_count
        pik_coors[1] /= pik_count
        if jp_coors[0] == 0:
            handler.jp.stop_moving()
            handler.jp.move_down()
        else:
            handler.jp.stop_moving_down()
            if jp_coors[0] - pik_coors[0] > 100:
                handler.jp.short_jump()
            elif jp_coors[1] - pik_coors[1] < -20:
                handler.jp.stop_moving_left()
                handler.jp.move_right()
            elif jp_coors[1] - pik_coors[1] > 20:
                handler.jp.stop_moving_right()
                handler.jp.move_left()

        #print(jp_coors[1] - pik_coors[1])
        #print(jp_coors)
        #print(pik_coors)

    def update_locs(self, locs, i, j):
        locs[0] += i
        locs[1] += j
