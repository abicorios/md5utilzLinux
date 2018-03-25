#!/usr/bin/env python3
exe='/usr/bin'
print("md5restorez v1.02 24.03.2017\nАвторы: omonim2007 и abicorios\nhttp://pscd.ru/forum/index.php?/topic/321-omonims-sety-dlia-retro-konsolei-8-64-bit")
print("https://github.com/abicorios")
print("Чтобы выйти нажмите Ctrl+C\nЧтобы скопировать или вставить используйте способ работающий в вашей командной строке.")
import os
import pandas as pd
from shutil import copyfile, move, rmtree
import hashlib
import subprocess, shlex
import re
def myrmtree(imypath):
    for r, d, f in os.walk(imypath):
        for i in f:
            os.chmod(r+'/'+i, 0o777)
    rmtree(imypath)
def myosremove(imypath):
    os.chmod(imypath, 0o777)
    os.remove(imypath)
def md5(myfile):
    hash_md5 = hashlib.md5()
    with open(myfile, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest().upper()
def drop(x,sep):
    return sep.join(x.split(sep)[:-1])
def isempty(folder):
    if len(os.listdir(folder))>0: return False
    else: return True
def p(a):
    print(a.replace(myfrom,'').replace(myto,'').replace(exe,'').replace(mybuffer,''))
    f.write(str(a)+'\n')
def nfolders(somepath):
    n=0
    for i in os.listdir(somepath):
        if os.path.isdir(i):
            n+=1
    return n
def narchives(somepath):
    n=0
    for i in os.listdir(somepath):
        if mytype(somepath)=='archive':
            n+=1
    return n
def mytype(ipath):
    if os.path.isfile(ipath):
        if re.search(r'\.(7z|zip|rar)$',ipath):
            return 'archive'
        else:
            return 'file'
    if os.path.isdir(ipath):
        return 'dir'
def inbuffer(ipath,ibuffer):
    if ibuffer in ipath:
        return True
    else:
        return False
    
def myrestore(ipath,ito,ibuffer):
    for i in os.listdir(ipath):
        thisthing=r'{}/{}'.format(ipath,i)
        #print('ipath={}, ito={}, ibuffer={}, mytype(thisthing)={}, thisthing={}'.format(ipath,ito,ibuffer,mytype(thisthing),thisthing))
        if mytype(thisthing)=='file':
            m=md5(thisthing)
            if m in list(t['md5']):
                for j in t[t['md5']==m].index:
                    if not os.path.isdir(r'{}/{}'.format(ito,drop(j,'/'))):
                        os.makedirs(r'{}/{}'.format(ito,drop(j,'/')))
                    #mytest(r'{}/{}'.format(ito,j))
                    p(copyfile(thisthing,r'{}/{}'.format(ito,j)))
                    t.loc[j,'processed']=1
            if m not in list(t['md5']):
                okpath=r'{}/{}'.format(notpath,i)
                if '.' in okpath.split('/')[-1]:
                    okpat=drop(okpath,'.')
                    h=okpath.split('.')[-1]
                else:
                    okpat=okpath
                    h=''
                if os.path.isfile(okpath):
                    i0=0
                    if h != '':
                        while os.path.isfile('{}{}.{}'.format(okpat,i0,h)):
                            i0+=1
                        p(copyfile(thisthing,'{}{}.{}'.format(okpat,i0,h)))
                    else:
                        while os.path.isfile('{}{}'.format(okpat,i0)):
                            i0+=1
                        p(copyfile(thisthing,'{}{}'.format(okpat,i0)))
                else:
                    p(copyfile(thisthing,okpath))
            if inbuffer(ipath,ibuffer):
                myosremove(thisthing)
        if mytype(thisthing)=='archive':
                mycmd='"{}/7z" x "{}" -o"{}" -aou'.format(exe,thisthing,ibuffer)
                p(mycmd)
                subprocess.run(shlex.split(mycmd))
                if inbuffer(ipath,ibuffer):
                    os.remove(thisthing)
                myrestore(ibuffer,ito,ibuffer)
        if mytype(thisthing)=='dir':
            #print('now thisthing is {}, and mytype(thisthing) is {}'.format(thisthing,mytype(thisthing)))
            if isempty(thisthing):
                if inbuffer(ipath,ibuffer):
                    os.rmdir(thisthing)
            else: #if not isempty(thisthing):
                myrestore(thisthing,ito,ibuffer)
mybuffer=r'/tmp/md5utilz'       
#mybuffer=r'/?\C:\Windows\Temp\md5utils'
if os.path.isdir(mybuffer): myrmtree(mybuffer)
#p7zx86=r'C:\Program Files (x86)\7-Zip'
#p7zx64=r'C:\Program Files\7-Zip'
while (not os.path.isfile(exe+'/7z')) or (not os.path.isfile('/usr/lib/p7zip/Codecs/Rar.so')):
    print('Установите p7zip-full и p7zip-rar чтобы возник испольняемый бинарный файл /usr/bin/7z способный работать с архивами 7z, zip и rar. Работа с rar обеспечивается благодаря файлу библиотеки /usr/lib/p7zip/Codecs/Rar.so')
    inp=str(input('Введите q чтобы выйти, или установите 7-Zip сейчас и введите здесь что угодно кроме q\n'))
    if inp=='q':
        exit()
#if os.path.isdir(p7zx64):
#    exe=p7zx64
#elif os.path.isdir(p7zx86):
#    exe=p7zx86
#else:
#    exit()
user=os.environ['USER']
myto=r'{}'.format(input('Введите путь к пустой папке, в которую нужно поместить результат, например /home/{}/roms by genre\n'.format(user)))
# myto='D:/test/00'
#myto=norm(myto)
#if os.path.isdir(myto): myrmtree(myto)
if not os.path.isdir(myto): os.mkdir(myto)
while len(os.listdir(myto))>0:
    print('Ошибка! Папка {} не пуста! \n'.format(myto))
    myto=r'{}'.format(input('Введите путь к пустой папке для размещения результата. Или введите q чтобы выйти.\n'))
    if myto=='q':
        exit()
#    myto=norm(myto)
mybase=r'{}'.format(input('Введите путь к файлу csv-базы, например /home/result/roms by genre ({}).csv\n'.format(pd.Timestamp.now().strftime('%d.%m.%Y'))))
# mybase=r'D:\test\0\long (04.03.2018).csv'
#mybase=U(mybase)
while not os.path.isfile(mybase):
    print('Ошибка! Файл {} не существует! \n'.format(mybase[4:]))
    mybase=r'{}'.format(input('Выберите актуальный файл csv-базы. Или введите q чтобы выйти.\n'))
    if mybase=='q':
        exit()
#    mybase=U(mybase)
# mybase=r'D:\t\Programs (11.02.2018).csv'
myfrom=r'{}'.format(input('Введите путь к источнику файлов, например D:/Good and NonGood roms\n'))
# myfrom='D:/test/long'
#myfrom=norm(myfrom)
while not os.path.isdir(myfrom):
    print('Ошибка! Папка {} не существует!\n'.format(myfrom[4:]))
    myfrom=r'{}'.format(input('Выберите актуальную папку. Или введите q чтобы выйти.\n'))
    if myfrom=='q':
        exit()
#    myfrom=norm(myto)
# myfrom=r'D:\Atari Jaguar\Programs'
f = open(r'{}\mylog.txt'.format(myto), 'a')
archive=0
while archive != 'yes' and archive != 'no':
    archive=str(input('Хотите добавить результаты в архивы? [yes|no]:\n'))
# archive='no'
if not os.path.isdir(mybuffer):os.mkdir(mybuffer)
#os.chdir(myfrom)
topath='{}/{}'.format(myto,drop(mybase.split('/')[-1],'.'))
notpath='{}/Not Included'.format(myto)
if not os.path.isdir(topath): os.mkdir(topath)
if not os.path.isdir(notpath): os.mkdir(notpath)
t=pd.read_csv(mybase)
t['path']=t['path'].str.replace('\\','/')
t=t.set_index('md5')
t['doubles']=t.index.value_counts()
t['pathname']=t['path']+'/'+t['name']
t=t.reset_index().set_index('pathname')
t['processed']=0
myrestore(myfrom,topath,mybuffer)
if archive=='yes':
    for i in set(t[t['processed']==1]['path']):
        thisthing=r'{}/{}'.format(topath,i)
        mycmd='"{}/7z" a "{}.7z" "{}/*" -mx9 -ms -sdel -mmt'.format(exe,thisthing,thisthing)
        p(mycmd)
        subprocess.run(shlex.split(mycmd))
        os.rmdir(thisthing)
os.chdir(myto)
myrmtree(mybuffer)
t=t[['path','name','md5','doubles','processed']]
t[t['doubles']>1].sort_values('md5').to_csv('doubles.csv',index=False)
t[t['processed']==0].to_csv('notfound.csv',index=False)
f.close()
input('Введите Enter чтобы выйти.\n')
