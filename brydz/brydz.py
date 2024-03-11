
from tkinter import *
from tkinter import messagebox
import os
import shutil



def stworz():
    def tworzy():
        naz = fol.get()
        if naz != "":
            try:
                naz="systemy\\"+naz
                os.makedirs(naz)
                for x in range(7):
                    os.makedirs(naz+"\\"+str(x+1)+"C")
                    os.makedirs(naz+"\\"+str(x+1)+"D")
                    os.makedirs(naz+"\\"+str(x+1)+"H")
                    os.makedirs(naz+"\\"+str(x+1)+"S")
                    os.makedirs(naz+"\\"+str(x+1)+"N")
                os.makedirs(naz+"\\KK")
                os.makedirs(naz+"\\RR")
                os.makedirs(naz+"\\PP")
                nazwij.destroy()
                main()
            except:
                #messagebox.showinfo(title="b³¹d", message="nazwa systemu ju¿ istnieje")
                messagebox.showinfo(title="blad", message="nazwa systemu juz istnieje")
                nazwij.destroy()
    def kop():
        def dod(prz,naz):
            zap=[]
            
            shutil.copytree("systemy\\"+prz.cget("text"), naz)
            
            nazwij.destroy()
            main()

        ac="nie"
        naz = fol.get()
        if naz!= "":
            for i in os.listdir("systemy"):
                if naz == i:
                    ac="tak"
            if ac != "tak":
                    naz="systemy//"+naz
                    wyb=Toplevel(nazwij)
                    #Label(wyb,text="które skopiowaæ?",font=f,width=rozmiar).grid()
                    Label(wyb,text="ktore skopiowac?",font=f,width=rozmiar).grid()
                    for i in os.listdir("systemy"):
                        c=Button(wyb,text=i,font=f,width=rozmiar)
                        c.config(command=lambda c=c:dod(c,naz))
                        c.grid()
            else:
                    #messagebox.showinfo(title="b³¹d", message="nazwa systemu ju¿ istnieje")
                    messagebox.showinfo(title="blad", message="nazwa systemu juz istnieje")
                    nazwij.destroy()
                
                
            
        
    nazwij=Toplevel(start)
    Label(nazwij,text="wpisz nazwe systemu",font=("a",10)).grid(row=0,column=0,columnspan=2)
    fol=Entry(nazwij)
    opcja1=Button(nazwij,text="ok",font=("a",10),command=lambda: tworzy())
    opcja2=Button(nazwij,text="skopiuj",font=("a",10),command=lambda: kop())
    fol.grid(row=1,column=0,columnspan=2)
    opcja1.grid(row=2,column=0)
    opcja2.grid(row=2,column=1)
    

def main():
    def usun(przycisk):
        #mes=messagebox.askquestion(title="potwierdz", message="czy chcesz usun¹æ "+ przycisk[0].cget("text"))
        mes=messagebox.askquestion(title="potwierdz", message="czy chcesz usunac "+ przycisk[0].cget("text"))
        if mes == "yes" :
            naz="systemy//"+przycisk[0].cget("text")
            shutil.rmtree(naz)
            main()

    for i in listbut:
        i.destroy()
    for i in listbut2:
        i.destroy()
    listbut.clear()
    listbut2.clear()
    
    linia=1
    Label(start,text="systemy brydzowe",width=rozmiar,font=f).grid(row=0,column=0,columnspan=2)

    for path in os.listdir("systemy"):
        a=Button(start,text=path,width=rozmiar,font=f)
        a.config(command= lambda a=a: main2(a))
        a.grid(row=linia,column=0)
        c=Button(start,text="del",font=f)
        c.config(command=lambda fol=(a,c) : usun(fol))
        c.grid(row=linia,column=1)
        linia+=1
        listbut.append(a)
        listbut2.append(c)
    

    b=Button(start,text="+ nowy",width=rozmiar,font=("a",25),command=stworz)
    b.grid(row=linia,column=0,columnspan=2)
    listbut2.append(b)
    

    

def main2(przycisk):#reakcja na zamkniêcie 
    def zablokuj():
            def kt():
                ktora=-1
                for x in range(-1,-len(historia)-1,-1):
                    if historia[x].cget("text")!="PASS" and historia[x].cget("text")!="X" and historia[x].cget("text")!="XX":
                        return ktora
                    else:
                        ktora-=1

            def przyciski():
                ktora=kt()
                try:
                    for x in range(len(but2)-3,-1,-1):
                        if but2[x].cget("text")==historia[ktora].cget("text"):
                            for i in range(x+1):
                                but2[i].config(state=DISABLED)

                except:
                    pass
            def liczby():
                try:

                    ktora=kt()
                    

                    for x in range(len(but)-1,-1,-1):
                        if historia[ktora].cget("text")[0]==but[x].cget("text"):
                            if historia[ktora].cget("text")[-1]!="T":
                                z=x
                            else:
                                z=x+1
                            for i in range(z):
                                but[i].config(state=DISABLED)
                        
                except:
                    pass
            def kontr():
                try:
                    if historia[-1].cget("text")=="PASS":
                        try:
                            if historia[-2].cget("text")=="X":
                                kontra.grid_forget()
                                pas.grid(padx=(45,1))
                            elif historia[-3].cget("text")=="X" and historia[-2].cget("text")=="PASS":
                                kontra.config(text="XX",bg="blue")
                                kontra.grid(row=0,column=5,sticky="w",padx=1)
                                pas.grid(padx=1) 
                            elif historia[-2].cget("text")!="PASS":
                                kontra.grid_forget()
                                pas.grid(padx=(45,1))
                            elif historia[-2].cget("text")=="PASS":
                                kontra.config(text="X",bg="#ba0f1a")
                                kontra.grid(row=0,column=5,sticky="w",padx=1)
                                pas.grid(padx=1)  
                        except:
                            kontra.grid_forget()
                            pas.grid(padx=(45,1))
                            kontra.config(text="X",bg="#ba0f1a")
                    
                    elif historia[-1].cget("text")=="X":
                        kontra.config(text="XX",bg="blue")
                        kontra.grid(row=0,column=5,sticky="w",padx=1)
                        pas.grid(padx=1)
                    elif historia[-1].cget("text")=="XX":
                        kontra.grid_forget()
                        pas.grid(padx=(45,1))
                        kontra.config(text="X",bg="#ba0f1a")
                    else:
                        kontra.config(text="X",bg="#ba0f1a")
                        kontra.grid(row=0,column=5,sticky="w",padx=1)
                        pas.grid(padx=1)  
                except:
                    kontra.config(text="X",bg="#ba0f1a")
                    kontra.grid_forget()
                    pas.grid(padx=(45,1))

            try:
                if historia[-1].cget("text")=="PASS" and historia[-2].cget("text")=="PASS" and historia[-3].cget("text")=="PASS":
                    if len(historia)!=3:
                        for x in but:
                            x.config(state=DISABLED)
                        for x in but2:
                            x.config(state=DISABLED)
                else:
                     przyciski()
                     liczby()
            except:
                pass

            kontr()

    def odblokuj():
        for i in but2:
            i.config(state=NORMAL)
        for i in but:
            i.config(state=NORMAL)
    
    def wypisz_tekst(l):
            def wpis(his):
                historia2=[]
                for q in his:
                    symbole=q.cget("text")
                    if symbole[-1]=="T":
                        symbole=symbole[0:2]
                    elif symbole[-1]=="X":
                        if len(symbole)==1:
                            symbole="KK"
                        else:
                            symbole="RR"
                    elif symbole=="PASS":
                        symbole="PP"
                    historia2.append(symbole)
                return historia2
            def inf(napis):
                
                test=''
                for i in range(len(napis)):
                   if napis[i]=="PASS":
                      napis[i]="P"   
                   test+=(napis[i]+"-")
                test=test[:-1]
                informacja.config(text=test)
                   
            tek.delete("1.0",END)
            nazwa=przycisk.cget("text")
            
            if l==-1:
                symbole=wpis(historia)
            else:
                symbole=wpis(historia[:l+1])
                
            global wcisniety
            wcisniety=l

            sumaw=''
            suma2=0
            suma3=0

            wszystko=False
            odp=False
            odp2=False
            odp3=False

            for sym in symbole:
                sumaw += sym
            if len(symbole)>=3:
                suma3=symbole[-3]+symbole[-2]+symbole[-1]
                suma2=symbole[-2]+symbole[-1]
            elif len(symbole)>=2:
                suma2=symbole[-2]+symbole[-1]
            
            pat="systemy//"+nazwa+"//"+symbole[-1]
            
            for path in os.listdir(pat):
                test=path[:-4]
                if test==sumaw:
                    wszystko=True
                    break
                elif test==suma3:
                    odp3=True
                elif test==suma2:
                    odp2=True
                elif test==symbole[-1]:
                    odp=True

             #inf jest to informacj¹ na dole aplikacji
            
            if wszystko:
                with open(pat+"//"+sumaw+".txt","r") as f:
                    tek.insert(END,f.read())
                test=[]
                if l!=-1:
                    for x in historia[:l+1]:
                        test.append(x.cget("text"))
                else:
                    for x in historia:
                        test.append(x.cget("text"))
                inf(test)

                #inf(test)    
            elif odp3:
                with open(pat+"//"+suma3+".txt","r") as f:
                    tek.insert(END,f.read())
                test=[historia[l-2].cget("text"),historia[l-1].cget("text"),historia[l].cget("text")] 
                
                inf(test)    
            elif odp2:
                with open(pat+"//"+suma2+".txt","r") as f:
                    tek.insert(END,f.read())
                
                test=[historia[l-1].cget("text"),historia[l].cget("text")] 
                inf(test)
            elif odp:
                with open(pat+"//"+test+".txt","r") as f:
                    tek.insert(END,f.read())

                test=historia[l].cget("text")
                inf([test])   
                
            else:
                tek.insert(END,"brak ustalen")

                test=historia[l].cget("text")
                print(test)
                inf([test])
            
              
            

    def linia(tek,b,f):   
        global ile, ilosc
        ile+=1
        
        

        if ile == 4:
            ile=0
            global frame1_2
            frame1_2=Frame(frame1,bg="black",height=wys2-250,width=szer2)
            frame1_2.pack(side=TOP)
            frame1_2.pack_propagate(0)
            historialin.append(frame1_2)
            a=Button(frame1_2,text=tek,font='Helvetica 9 bold',bg=b,fg=f,height=wysb,width=szerb)
            
            a.config(command=lambda i=ilosc:wypisz_tekst(i))
            a.pack(side=LEFT,padx=(szo2,szo))
        else:
            a=Button(historialin[-1],text=tek,font='Helvetica 9 bold',bg=b,fg=f,height=wysb,width=szerb)
            
            a.config(command=lambda i=ilosc:wypisz_tekst(i))
            a.pack(side=LEFT,padx=szo)
        
        ilosc+=1    
        
        historia.append(a)
        zablokuj()
        wypisz_tekst(-1)
    def cyfra(x):
        
        
        for i in but:
            i.config(state=NORMAL,bg="grey")
        for i in but2:
            i.config(state=NORMAL)
          
        
        but[x].config(state=DISABLED,bg="white")
        licz=str(x+1)
        trefl.config(text=licz+"C")
        karo.config(text=licz+"D")
        kier.config(text=licz+"H")
        pik.config(text=licz+"S")
        nt.config(text=licz+"NT")
        zablokuj()
        
    nazwa=przycisk.cget("text")
    start.withdraw()

    licytacja = Toplevel(start)
    licytacja.resizable(False,False)
    licytacja.title(nazwa)  
    def otw():
        start.deiconify()
        licytacja.destroy()
    licytacja.protocol("WM_DELETE_WINDOW",otw)

    szer=500
    wys=100
    frame1=Frame(licytacja,bg="Pink",height=wys,width=szer,pady=20)
    frame2=Frame(licytacja,bg="pink",height=150,width=szer)
    frame3=Frame(licytacja,bg="pink",height=200,width=szer)
    frame1.pack(side=TOP,expand=True,fill=X)
    frame2.pack(side=TOP,fill=X)
    frame3.pack(side=TOP,fill=X)
    

    # E N W S
    szer2=int(800/3) 
    wys2=300 
    szo=int(szer2/20)
    szo2=int(szo/2)+15
    szerb=4
    szerl=4
    wysb=int(wys2/150)
    wysl=int(wys2/200)
    frame1_1=Frame(frame1,bg="white",width=szer2,height=int(wys2/10))
    frame1_1.pack(side=TOP,expand=False)
    frame1_1.pack_propagate(0)
    frame3.pack_propagate(0)

    Label(frame1_1,text="E",bg="white",height=wysl,width=szerl).pack(side=LEFT,padx=(szo2,szo))
    Label(frame1_1,text="S",bg="white",height=wysl,width=szerl).pack(side=LEFT,padx=(szo+5,szo))
    Label(frame1_1,text="W",bg="white",height=wysl,width=szerl).pack(side=LEFT,padx=(szo+5,szo))
    Label(frame1_1,text="N",bg="white",height=wysl,width=szerl).pack(side=LEFT,padx=(szo+2,0))
    
    
   
    # wybor
    szer3=int(szer/2)
    wys3=110
    wid=4
    hig=2
    w=10
    srodek=Frame(frame2,bg="grey",width=szer3)
    srodek1=Frame(srodek,bg="grey",width=1000,height=100)
    srodek2=Frame(srodek,bg="grey",width=1000,height=100)
    
    srodek.pack(side=LEFT,anchor="n",expand=False,pady=(20,0),padx=(100,20))
    srodek1.pack(side=TOP,pady=(10,0),padx=(20))
    srodek2.pack(side=TOP,pady=(10,10),padx=(20))
    

    jen=Button(srodek1,text="1",width=wid,height=hig,font=("a",w),command=lambda:cyfra(0),state=DISABLED,bg="white",fg="white")
    dwa=Button(srodek1,text="2",width=wid,height=hig,font=("a",w),command=lambda:cyfra(1),bg="grey",fg="white")
    trzy=Button(srodek1,text="3",width=wid,height=hig,font=("a",w),command=lambda:cyfra(2),bg="grey",fg="white")
    czt=Button(srodek1,text="4",width=wid,height=hig,font=("a",w),command=lambda:cyfra(3),bg="grey",fg="white")
    pie=Button(srodek1,text="5",width=wid,height=hig,font=("a",w),command=lambda:cyfra(4),bg="grey",fg="white")
    sze=Button(srodek1,text="6",width=wid,height=hig,font=("a",w),command=lambda:cyfra(5),bg="grey",fg="white")
    siem=Button(srodek1,text="7",width=wid,height=hig,font=("a",w),command=lambda:cyfra(6),bg="grey",fg="white")

    but=(jen,dwa,trzy,czt,pie,sze,siem)

    jen.grid(row=0,column=0,sticky="w")
    dwa.grid(row=0,column=1,sticky="w")
    trzy.grid(row=0,column=2,sticky="w")
    czt.grid(row=0,column=3,sticky="w")
    pie.grid(row=0,column=4,sticky="w")
    sze.grid(row=0,column=5,sticky="w")
    siem.grid(row=0,column=6,sticky="w")

    licz=str(1)


    global ile,ilosc

    
    ilosc=0
    ile=3

    fonto='Helvetica 10 bold'

    historia=[]
    historialin=[]

    trefl=Button(srodek2,text=(licz+"C"),width=wid,height=hig,bg="#74db9b",fg="#18731d",font=fonto)
    karo=Button(srodek2,text=(licz+"D"),width=wid,height=hig,bg="#edbd7e",fg="#c7750a",font=fonto)
    kier=Button(srodek2,text=(licz+"H"),width=wid,height=hig,bg="#de787f",fg="#e80740",font=fonto)
    pik=Button(srodek2,text=(licz+"S"),width=wid,height=hig,bg="#2a6fc9",fg="#072245",font=fonto)
    nt=Button(srodek2,text=(licz+"NT"),width=wid,height=hig,font=fonto)
    kontra=Button(srodek2,text="X",width=wid,height=hig,bg="#ba0f1a",fg="white",font=fonto)
    pas=Button(srodek2,text="PASS",width=wid+2,height=hig,bg="green",fg="white",font=fonto)

    but2=(trefl,karo,kier,pik,nt,kontra,pas)

    trefl.config(command=lambda :linia(trefl.cget("text"),trefl.cget("bg"),trefl.cget("fg")) )
    karo.config(command=lambda :linia(karo.cget("text"),karo.cget("bg"),karo.cget("fg")) )
    kier.config(command=lambda :linia(kier.cget("text"),kier.cget("bg"),kier.cget("fg")) )
    pik.config(command=lambda :linia(pik.cget("text"),pik.cget("bg"),pik.cget("fg")) )
    nt.config(command=lambda :linia(nt.cget("text"),nt.cget("bg"),nt.cget("fg")) )
    kontra.config(command=lambda :linia(kontra.cget("text"),kontra.cget("bg"),kontra.cget("fg")) )
    pas.config(command=lambda :linia(pas.cget("text"),pas.cget("bg"),pas.cget("fg")) )

    trefl.grid(row=0,column=0,sticky="w",padx=1)
    karo.grid(row=0,column=1,sticky="w",padx=1)
    kier.grid(row=0,column=2,sticky="w",padx=1)
    pik.grid(row=0,column=3,sticky="w",padx=1)
    nt.grid(row=0,column=4,sticky="w",padx=(1,40))
    #kontra.grid(row=0,column=5,sticky="w",padx=1)
    pas.grid(row=0,column=6,sticky="w",padx=(45,1))

    
    #pas.grid(padx=(45,1))
    #pas.grid(padx=1)



    #alert i back

    def cofnij():
        global ile,ilosc
        try:
            historia[-1].destroy()
            historia.pop(-1)
            ile-=1
            ilosc-=1
            

            if ile==-1:
                ile=3
                historialin[-1].destroy()
                historialin.pop(-1)
        except:
            pass
        odblokuj()
        zablokuj()
    def usun():
        global ile,ilosc
        mes=messagebox.askquestion(title="potwierdz", message="czy chcesz wszystko usunac")
        if mes=="yes":
            for i in historialin:
                i.destroy()
            ile=3
            ilosc=0
            historialin.clear()
            historia.clear()
            kontra.grid_forget()
            pas.grid(padx=(45,1))
            informacja.config(text='')
            tek.delete("1.0",END)
    
    #zapisuje alert        
    def  zapisz():
        global wcisniety
        try:
            test=''
            if wcisniety!=-1:
                for x in historia[:wcisniety+1]:
                    w=x.cget("text")
                    if w=="PASS":
                        w="P"
                    test+=(w+"-")
            else: 
                for x in historia:
                    w=x.cget("text")
                    if w=="PASS":
                        w="P"
                    test+=(w+"-")
            test=test[:-1]

            wys=2
            szer2=15
            szer1=szer2*3+2
            f=("a",10)
            dodaj=Toplevel(licytacja)
            dodaj.title("alert")  
            frala1=Frame(dodaj)
            frala1.pack(side=TOP)
            frala2=Frame(dodaj)
            frala2.pack(side=TOP)
            one=Button(frala1,text="cala konwencja\n"+test,height=wys,width=szer1,font=f)

            one.pack()
            one.config(command=lambda: plik(0))

            try:#sprawdzanie mo¿liwosci 2 lub wiecej
                tre=Button(frala2,text=historia[wcisniety-1].cget("text")+"-"+historia[wcisniety].cget("text"),height=wys,width=szer2,font=f)
                two=Button(frala2,text=historia[wcisniety].cget("text"),height=wys,width=szer2,font=f)


                two.pack(side=LEFT)
                tre.pack(side=LEFT)
                two.config(command=lambda: plik(1))
                tre.config(command=lambda: plik(2))
                try:
                    czw=Button(frala2,text=historia[wcisniety-2].cget("text")+"-"+historia[wcisniety-1].cget("text")+"-"+historia[wcisniety].cget("text"),height=wys,width=szer2,font=f)
                    
                    
                    czw.pack(side=LEFT)
                    czw.config(command=lambda: plik(3))
                except:
                    pass
            except:
                pass
            
            
            def plik(opcja):
                def wpis(his):
                    historia2=[]
                    for q in his:
                        symbole=q.cget("text")
                        if symbole[-1]=="T":
                            symbole=symbole[0:2]
                        elif symbole[-1]=="X":
                            if len(symbole)==1:
                                symbole="KK"
                            else:
                                symbole="RR"
                        elif symbole=="PASS":
                            symbole="PP"
                        historia2.append(symbole)
                    return historia2
                if wcisniety!=-1:
                    sym=wpis(historia[:wcisniety+1])
                else:
                    sym=wpis(historia)
                print(sym)
            
            
            
        except:#koniec alerta
            pass

    fr=Frame(frame2)
    fr.pack(side=LEFT,anchor="e",pady=(18,0),padx=(0,10))
    alert=Button(fr,width=7,height=4,bg="green",text="!\nALERT",fg="white",command=zapisz)
    back=Button(fr,width=7,height=1,bg="white",text="<<",fg="black",command=cofnij)
    delete=Button(fr,width=7,height=1,bg="white",text="del",fg="black",command=usun)

    delete.pack(side=TOP)
    alert.pack(side=TOP)
    back.pack(side=TOP)
    #tekst

    tek=Text(frame3,width=80,height=30)
    informacja=Label(frame3,height=1,text="",font=("a",8),fg="black",bg="pink")
    informacja.pack(side=BOTTOM)
    tek.pack(side=TOP,pady=(20,0),padx=10)
    

start = Tk()
start.title("system")

rozmiar=20
f=("a",20)
listbut=[]
listbut2=[]



main()


start.mainloop()



