
class Person(object):
    def __init__(self,name):
        super(Person, self).__init__()
        self.name = name
        self.gun = None
        self.hp = 100
    def anzhuang_zidan(self,danjia_temo,zidan_temo):
        '''把子弹装到弹夹中'''
        #弹夹保存子弹
        danjia_temo.baocun_zidan(zidan_temo)
    def anzhuang_danjia(self,gun_temp,danjia_temp):
        gun_temp.baocun_danjia(danjia_temp)
    def na_qiang(self,gun_temp):
        self.gun = gun_temp
    def __str__(self):
        if self.gun:
            return "%s 的血量为：%d 他有枪,%s"%(self.name,self.hp,self.gun)
        else:
            if self.hp>0:
                return "%s 的血量为：%d 他没枪"%(self.name,self.hp)
            else:
                return "%s 已死。。。"%(self.name)
    def koubanji(self,diren):
        self.gun.kaihuo(diren)
    def diaoxue(self,shashangli):
        self.hp-=shashangli
class Gun(object):
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name = name
        self.danjia = None
    def baocun_danjia(self,dan_jia):
        self.danjia = dan_jia
    def __str__(self):
        if self.danjia:
            return "枪的信息为：%s %s"%(self.name,self.danjia)
        else:
            return "枪的信息为：%s 这把枪没有弹夹"%(self.name)
    def kaihuo(self,diren):
        '''枪从弹夹中获取子弹，子弹击中敌人'''
        #先从弹夹中取子弹
        zidan_temp = self.danjia.tanchu_zidan()
        #用子弹上海敌人
        if zidan_temp:
            zidan_temp.dazhong(diren)
        else:
            print("弹夹中没有子弹了。。。。。")
class Danjia(object):
    def __init__(self,max_num):
        self.max_num = max_num
        self.zidan_list = []
    def baocun_zidan(self,zidan_temp):
        self.zidan_list.append(zidan_temp)
    def __str__(self):
        return "弹夹的信息为：%d/%d"%(len(self.zidan_list),self.max_num)
    def tanchu_zidan(self):
        '''弹出最上面的那颗子弹'''
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None
class Zidan(object):
    def __init__(self,shanghai):
        self.shanghai = shanghai
    def dazhong(self,diren):
        diren.diaoxue(self.shanghai)
        #diren.hp-=diren.hp-self.shanghai
def main():
    #1.创建一个老王
    lao_wang = Person('lao_wang')
    #2.创建一个抢
    ak47 = Gun("ak47")
    #3.创建一个弹夹
    dan_jia = Danjia(100)
    #4.创建一些子弹
    for i in range(15):
        zidan = Zidan(10)
    #5.创建一个敌人
    gebi_laosong = Person("隔壁老宋")
    #print(gebi_laosong)
    #6.老王把子弹安装到弹夹
    for i in range(15):
        lao_wang.anzhuang_zidan(dan_jia, zidan)
    #print(dan_jia)
    #print(ak47)
    #7.老王把弹夹安装到抢中
    lao_wang.anzhuang_danjia(ak47,dan_jia)
    #print(ak47)
    #8.老王拿起枪
    lao_wang.na_qiang(ak47)
    #print(lao_wang)

    #9.老王开枪
    #9.1老王扣扳机（老宋）
    lao_wang.koubanji(gebi_laosong)
    print(ak47)
    print(gebi_laosong)
    lao_wang.koubanji(gebi_laosong)
    print(ak47)
    print(gebi_laosong)
    lao_wang.koubanji(gebi_laosong)
    print(ak47)
    print(gebi_laosong)
    lao_wang.koubanji(gebi_laosong)
    print(ak47)
    print(gebi_laosong)
    lao_wang.koubanji(gebi_laosong)
    print(ak47)
    print(gebi_laosong)
    lao_wang.koubanji(gebi_laosong)
    print(ak47)
    print(gebi_laosong)
    lao_wang.koubanji(gebi_laosong)
    print(ak47)
    print(gebi_laosong)
    lao_wang.koubanji(gebi_laosong)
    print(ak47)
    print(gebi_laosong)
    lao_wang.koubanji(gebi_laosong)
    print(ak47)
    print(gebi_laosong)
    lao_wang.koubanji(gebi_laosong)
    print(ak47)
    print(gebi_laosong)


if __name__ == '__main__':
    main()
