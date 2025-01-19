import tkinter
import random
import time

masu = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
shirusi = 0
kachi = 0
FNT = ("Times New Roman", 60)

def masume():
  cvs.delete("all")
  for i in range(1,3):
    cvs.create_line(200*i,0,200*i,600, fill="gray",width=8)
    cvs.create_line(0,200*i,600,200*i, fill="gray",width=8)
  for y in range(3):
    for x in range(3):
      X = x * 200
      Y = y * 200
      if masu[y][x] == 1:
        cvs.create_oval(X+20,Y+20,X+180,Y+180,outline="blue",width=12)
      if masu[y][x] == 2:
        cvs.create_line(X+20,Y+20,X+180,Y+180,fill="red",width=12)
        cvs.create_line(X+180,Y+20,X+20,Y+180,fill="red",width=12)

  if shirusi == 0:
    cvs.create_text(300,300,text="スタート",fill="navy",font=FNT)
  cvs.update()

def click(e):
  global shirusi
  if shirusi == 9:
    replay()
    return
  if shirusi == 1 or shirusi == 3 or shirusi == 5 or shirusi == 7:
    return
  mx = int(e.x/200)
  my = int(e.y/200)
  if mx>2: mx = 2
  if my>2: my = 2
  if masu[my][mx] == 0:
    masu[my][mx] = 1
    shirusi += 1
    masume()
    time.sleep(0.5)
    hantei()
    syouhai()
    if shirusi < 9:
      computer()
      masume()
      time.sleep(0.5)
      hantei()
      syouhai()

def computer():
  global shirusi
  for y in range(3):
    for x in range(3):
      if masu[y][x] == 0:
        masu[y][x] = 2
        hantei()
        if kachi == 2:
          shirusi += 1
          return
        masu[y][x] = 0
  for y in range(3):
    for x in range(3):
      if masu[y][x] == 0:
        masu[y][x] = 1
        hantei()
        if kachi == 1:
          masu[y][x] = 2
          shirusi += 1
          return
        masu[y][x] = 0
  while True:
    x = random.randint(0,2)
    y = random.randint(0,2)
    if masu[y][x] == 0:
      masu[y][x] = 2
      shirusi += 1
      break

def hantei():
  global kachi
  kachi = 0
  for n in range(1,3):
    if masu[0][0] == n and masu[0][1] == n and masu[0][2] == n:
      kachi = n
    if masu[1][0] == n and masu[1][1] == n and masu[1][2] == n:
      kachi = n
    if masu[2][0] == n and masu[2][1] == n and masu[2][2] == n:
      kachi = n
    if masu[0][0] == n and masu[1][0] == n and masu[2][0] == n:
      kachi = n
    if masu[0][1] == n and masu[1][1] == n and masu[2][1] == n:
      kachi = n
    if masu[0][2] == n and masu[1][2] == n and masu[2][2] == n:
      kachi = n
    if masu[0][0] == n and masu[1][1] == n and masu[2][2] == n:
      kachi = n
    if masu[0][2] == n and masu[1][1] == n and masu[2][0] == n:
      kachi = n
def syouhai():
  global shirusi
  if kachi == 1:
    cvs.create_text(300,300,text="あなたの勝ち",font=FNT,fill="cyan")
    shirusi = 9
  if kachi == 2:
    cvs.create_text(300,300,text="コンピュータの勝ち",font=FNT,fill="pink")
    shirusi = 9
  if shirusi == 9 and kachi == 0:
    cvs.create_text(300,300,text="引き分け",font=FNT,fill="lime")

def replay():
  global shirusi
  shirusi = 0
  for y in range(3):
    for x in range(3):
      masu[y][x] = 0
  masume()

root = tkinter.Tk()
root.title("三目並べ")
root.resizable(False,False)
root.bind("<Button>",click)
cvs = tkinter.Canvas(width=600,height=600,bg="white")
cvs.pack()
masume()
root.mainloop()