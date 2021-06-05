import pygame
pygame.init()
from plane_sprites import *
# 创建飞机大战游戏主类


class PlaneGame(object):
    # 初始化方法
    def __init__(self):
        print("初始化游戏")
        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN.size)
        # 2.创建时钟
        self.clock = pygame.time.Clock()
        # 3.私有方法，创建精灵、精灵组
        self.__create_sprite()
        # 调用set_timer （定时器方法）设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(CREATE_FIRE_EVENT, 500)
    # 私有方法
    def __create_sprite(self):
        # 创建背景精灵和精灵组
        bg1 = BackGroud()
        bg2 = BackGroud(True)
        self.back_ground = pygame.sprite.Group(bg1, bg2)
        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄的精灵精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
    # 开始游戏方法
    def start_game(self):
        print("游戏开始...")

        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新绘制精灵组
            self.__update_sprites()
            # 5.刷新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
               PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出现")
                # 1.创建敌机精灵
                enemy = Enemy()
                # 2.将敌机精灵添加到精灵组
                self.enemy_group.add(enemy)
            elif event.type == CREATE_FIRE_EVENT:
                self.hero.fire()
        # 使用键盘模块提供的获取按键方法 -按键元祖
        keys_pressed = pygame.key.get_pressed()
        # 判断元祖中按键对应的索引为1
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表是否有内容
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        # 精灵组调用update，draw方法
        self.back_ground.update()
        self.back_ground.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()


