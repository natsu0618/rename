# -*- coding: UTF-8 -*-
import os,sys


def rename():
    try:
        while True:
            path=input("请输入文件夹的绝对路径(输入0退出)：")
            if path=="0":   #循环程序，让用户决定退出与否
                break  
            filelist=os.listdir(path)   #避免奇葩用户乱输入，先尝试打开路径
            if path!="0":   #改名代码
                name=input("请输入名字(如特摄;芜湖;旅游等,可跳过)：")   #这里可以随便输入所以不管
                while True: #这里防止用户不输入阿拉伯数字去输入一些奇奇怪怪的东西 
                    startnum=input("从什么数字开始命名(请输入阿拉伯数字,跳过默认为1)：")
                    if len(startnum)<=0:
                        startnum=1
                    try:
                        int(startnum)
                        break
                    except ValueError:
                        print("请输入正确的阿拉伯数字。")   
                while True: #防止用户不输入后缀名  
                    filetype=input("请输入后缀名(如.jpg;.png;.mp4等)：")
                    if len(filetype)<=0:
                        print("请输入后缀名！！！") 
                    else:
                        break   
                while True: #防止用户不输入阿拉伯数字，这里要输入位数       
                    digit=input("你希望生成几位数的文件名(默认为3位数)：") 
                    if len(digit)<=0:
                        digit=3
                    try:
                        int(digit)
                        break
                    except ValueError:
                        print("请输入正确的阿拉伯数字。")      

                print("正在生成以"+name+str(f"%0{digit}d" % startnum)+filetype+"格式的文件名")    

                i=0
                for files in filelist:
                    Olddir=os.path.join(path,files)
                    if os.path.isdir(Olddir):
                        continue
                    numbers=i+int(startnum)
                    Newdir=os.path.join(path,name+str(f"%0{digit}d" % numbers)+filetype)
                    os.rename(Olddir,Newdir)
                    i+=1
                print("一共修改了"+str(i)+"个文件")
                    
    except FileNotFoundError:   #避免奇葩用户乱输入，先尝试打开路径
        print("系统找不到指定路径，请输入正确的路径。")
        return rename()
    except OSError:    #避免奇葩用户乱输入，先尝试打开路径
        print("系统找不到指定路径，请输入正确的路径。")
        return rename() 


rename()

