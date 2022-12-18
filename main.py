import sys
import random
import player
import time


class Loveletter(object):

    def __init__(self):
        self.player1 = player.Player()
        self.player2 = player.Player()
        self.player1.setplayernum(self.player1, 1)
        self.player2.setplayernum(self.player2, 2)

    def start(self):

        poker1 = ["卫兵", "卫兵", "卫兵", "卫兵", "卫兵", "牧师", "牧师",
                  "男爵", "男爵", "侍女", "侍女", "王子", "王子", "国王", "伯爵夫人", "公主"]  # 生成一副整牌
        # 移除三张牌
        random.shuffle(poker1)  # 洗牌
        del poker1[0:2]
        player.Player().getpoker(poker1)  # 传递牌库
        #print("初始化牌堆是  %s" % poker1)
        self.player1.drawcard()
        self.player2.drawcard()
        # print("玩家1的手牌是%s  " % self.player1.gethandcard())
        # print("玩家2的手牌是%s  " % self.player2.gethandcard())
        # print("第一回合牌库%s  " % self.poker1)

    def enterround(self):
        winconditions = 0
        playerround = 1
        while winconditions != 1 and 2:
            self.player1.drawcard()
            while playerround == 1:
                print("玩家1现在的手牌是%s" % self.player1.gethandcard())
                # 判断侍女是否被使用
                if winconditions == 4:
                    print("对手使用了侍女牌，你无法对他造成伤害，选择弃掉的手牌，0或1")
                    caozuo = input()
                    print("玩家1弃掉了%s" % self.player1.handcard[int(caozuo)])
                    winconditions = self.player1.discard(self.player1, int(caozuo))
                else:
                    print("使用哪张牌?  输入0是第一张，1是第二张牌")
                    caozuo = input()
                    print("玩家1使用了%s" % self.player1.handcard[int(caozuo)])
                    time.sleep(0.5)
                    winconditions = self.player1.usecard(int(caozuo), self.player1, self.player2)  # 玩家使用卡牌
                # print("在玩家1循环中winconditions:", winconditions, "playerround", playerround)

                if winconditions == 8:
                    # 如果是公主就继续玩家1
                    continue
                if winconditions == 0 or winconditions == 4:
                    # 如果是0代表卡牌使用，进入玩家2阶段
                    playerround = 2
                if winconditions == 1 or winconditions == 2:
                    playerround = 0

            # print("大循环中winconditions:", winconditions, "playerround", playerround)
            # 玩家2操作
            '''
            while playerround == 2:
                # print("winconditions:", winconditions)
                self.player2.drawcard()
                print("玩家2现在的手牌是%s" % self.player2.gethandcard())
                print("使用哪张牌?  输入0是第一张，1是第二张牌")
                caozuo = input()
                print("玩家2使用了%s" % self.player2.handcard[int(caozuo)])
                winconditions = self.player2.usecard(int(caozuo), self.player2, self.player1)  # 玩家使用卡牌
                if winconditions == 8:
                    pass
                if winconditions == 0:
                    # print()
                    playerround = 1
                if winconditions == 1 or 2:
                    playerround = 0
            '''
            # 电脑操作
            self.player2.drawcard()
            while playerround == 2:
                print("现在由玩家2(电脑)操作")
                time.sleep(0.6)
                if winconditions == 4:
                    print("玩家使用了侍女牌，电脑无法对他造成伤害，选择弃掉的手牌")
                    caozuo = random.randint(0, 1)
                    time.sleep(0.6)
                    print("电脑弃掉了%s" % self.player2.handcard[int(caozuo)])
                    winconditions = self.player2.discard(self.player2, int(caozuo))
                else:
                    caozuo = random.randint(0, 1)
                    time.sleep(0.6)
                    print("玩家2使用了%s" % self.player2.handcard[caozuo])
                    winconditions = self.player2.usecard(caozuo, self.player2, self.player1)  # 玩家使用卡牌

                if winconditions == 8:
                    continue
                if winconditions == 0 or winconditions == 4:
                    # 进入玩家1阶段
                    playerround = 1
                if winconditions == 1 or winconditions == 2:
                    playerround = 0

                # print("在玩家2循环中winconditions:", winconditions, "playerround", playerround)

            if playerround == 0:
                break
        return winconditions

    def gameover(self, playeri):
        print("游戏结束")
        time.sleep(0.6)
        if playeri == 1:
            print("玩家1获胜", playeri)
            input()
        else:
            print("玩家2获胜", playeri)
            input()


playeri = 0
game = Loveletter()
game.start()  # 游戏开始
winplayer = game.enterround()  # 进入回合
game.gameover(winplayer)
