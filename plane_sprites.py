import random
import pygame
# 屏幕大小常亮
SCREEN = pygame.Rect(0, 0, 480, 700)
# 刷新帧率常量
FRAME_PER_SEC = 60
# 创建敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建英雄发射子弹事件常量
CREATE_FIRE_EVENT = pygame.USEREVENT + 1

# 创建飞机大战精灵子类(参数为 image_name, speed)


class GameSprite(pygame.sprite.Sprite):

    #重写初始化方法 -> 图像load，rect，speed

    def __init__(self, image_name, speed = 1):
        # 重写前调用父类初始化方法
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    # 重写update方法
    def update(self):
        # 更新图像移动速度
        self.rect.y += self.speed
# 创建背景精灵的子类，继承自精灵子类

class BackGroud(GameSprite):
    def __init__(self, is_alt=False):
        # 调用父类的初始化方法创建(image/rect/speed)
        super().__init__("E:/pythonjob/pythonProject/plane/images/background.png")
        # 判断是否为替换的图像，如果是设置位置
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        # 1.调用精灵子类的方法实现
        super().update()

        # 2.判断是否移出屏幕，如果移出屏幕，将背景设置到屏幕正上方
        if self.rect.y >= SCREEN.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):

    def __init__(self):

        # 1.调用父类方法，创建敌机精灵
        super().__init__("E:/pythonjob/pythonProject/plane/images/enemy1.png")
        # 2.指定敌机的初始速度
        self.speed = random.randint(2, 3)
        # 3.指定敌机的初始位置
        self.rect.bottom = 0
        max_x = SCREEN.width - self.rect.width
        self.rect.x = random.randint(0, max_x)


    def update(self):
        # 1.调用父类方法保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是从精灵组删除
        if self.rect.y >= SCREEN.height:
            # print("飞出屏幕，需要从精灵组删除...")
            # kill 方法可以将精灵从精灵组删除，并销毁对象，释放内存
            self.kill()

    def __del__(self):
        pass
        # print("敌机挂了 %s" % self.rect)

class Hero(GameSprite):
    def __init__(self):
        # 1.调用父类方法，设置图像速度
        super().__init__("E:/pythonjob/pythonProject/plane/images/me1.png", 0)
        # 2.设置英雄的出位置
        self.rect.centerx = SCREEN.centerx
        self.rect.bottom = SCREEN.bottom - 120
        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄在水平方向移动
         self.rect.x += self.speed
        # 控制英雄不能离开屏幕
         if self.rect.x < 0:
             self.rect.x = 0
         elif self.rect.right > SCREEN.width:
             self.rect.right = SCREEN.width

    def fire(self):
        print("发射子弹..")
        for i in (0, 1, 2):
            # 1.创建子弹精灵
            bullet = Bullet()
            # 2.设置子弹精灵位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3.将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    # 子弹精灵
    def __init__(self):
        # 调用父类方法设置子弹位置、速度
        super().__init__("E:/pythonjob/pythonProject/plane/images/bullet1.png", -2)

    def update(self):
        # 调用父类方法让子弹垂直飞行
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁..")
