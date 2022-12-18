from random import randint
import time

class Player(object):
    poker1 = []  # 牌堆

    def __init__(self):
        self.handcard = []
        self.playernum = 0

    def getpoker(self, poker):  # 获取牌堆
        Player.poker1 = poker
        return

    def setplayernum(self, player, i):  # 设置玩家编号
        player.playernum = i

    def getpplayernum(self):  # 获取玩家编号
        return self.playernum  ##### self就是实例对象本身！！！！

    def gethandcard(self):  # 获取玩家手牌
        return self.handcard

    def getcardnum(self, card):  # 获取玩家手牌牌面数字
        if card == "卫兵":
            return 1
        if card == "牧师":
            return 2
        if card == "男爵":
            return 3
        if card == "侍女":
            return 4
        if card == "王子":
            return 5
        if card == "国王":
            return 6
        if card == "伯爵夫人":
            return 7
        if card == "公主":
            return 8

    def drawcard(self, player):  # 抽卡 哪位玩家的手牌
        player.handcard.append(Player.poker1[0])
        del Player.poker1[0]

    def usecard(self, i, player1, player2):  # 使用卡牌 第几张手牌，使用玩家，被使用玩家

        if player1.handcard[i] == "卫兵":
            xuanze = 0
            if player1.playernum == 1:
                print("你选择对手是哪一张牌？请打牌面编号1-8")
                xuanze = int(input())
                if xuanze == player2.getcardnum(player2.handcard[0]):
                    print("你猜中了电脑的手牌")
                    del player1.handcard[0]
                    return 1
                else:
                    del player1.handcard[0]
                    print("你猜错了电脑的手牌")
                    return 0
            if player1.playernum == 2:
                xuanze = randint(1, 8)
                if xuanze == player2.getcardnum(player2.handcard[0]):
                    print("电脑猜中了你的手牌")
                    del player1.handcard[0]
                    return 2
                else:
                    del player1.handcard[0]
                    return 0

        elif player1.handcard[i] == "牧师":
            time.sleep(0.6)
            print("对方的手牌为%s" % player2.gethandcard())
            del player1.handcard[0]
            return 0

        elif player1.handcard[i] == "男爵":
            del player1.handcard[i]
            if player1.playernum == 1:
                time.sleep(0.6)
                print("对方的手牌为%s，你的手牌为%s" % (player2.handcard[0] , player1.handcard[0]))
                if player1.getcardnum(player1.handcard[0]) > player2.getcardnum(player2.handcard[0]):
                    print(1)
                    return 1
                elif player1.getcardnum(player1.handcard[0]) < player2.getcardnum(player2.handcard[0]):
                    print(2)
                    return 2
                else:
                    return 0

            if player1.playernum == 2:
                time.sleep(0.6)
                print("电脑的手牌为%s，你的手牌为%s" % (player1.handcard[0] , player2.handcard[0]))
                if player1.getcardnum(player1.handcard[0]) > player2.getcardnum(player2.handcard[0]):
                    return 2
                elif player1.getcardnum(player1.handcard[0]) < player2.getcardnum(player2.handcard[0]):
                    return 1
                else:
                    return 0

        elif player1.handcard[i] == "侍女":
            del player1.handcard[i]
            return 4

        elif player1.handcard[i] == "王子":
            del player1.handcard[i]
            time.sleep(0.6)
            print("对方弃掉了%s" % player2.handcard[0])
            player2.discard(player2, 0)
            player2.drawcard(player2)
            return 0

        elif player1.handcard[i] == "国王":
            time.sleep(0.6)
            print("交换双方手牌")
            del player1.handcard[i]
            a1 = player1.handcard[0]
            player1.handcard[0] = player2.handcard[0]
            player2.handcard[0] = a1
            return 0

        elif player1.handcard[i] == "伯爵夫人":
            player1.discard(player1, i)
            del player1.handcard[0]
            return 0

        elif player1.handcard[i] == "公主":
            time.sleep(0.6)
            print("你不能主动使用公主")
            return 8

    def discard(self, player, i):  # 哪位玩家弃牌 弃第二张牌
        if player.handcard[i] == "公主":
            time.sleep(0.6)
            print("弃置手牌",player.handcard[i])

            return player.playernum
        else:
            time.sleep(0.6)
            print("弃置手牌", player.handcard[i])
            player.drawcard(player)
            del player.handcard[i]
            return 0

