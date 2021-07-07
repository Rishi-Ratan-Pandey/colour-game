from tkinter import*
import pygame
from tkinter import messagebox
import random
pygame.mixer.init()
root=Tk()
root.geometry('575x200')
point=0
point_data=IntVar()
time_left_data=IntVar()
time_left=60
check=True
time_left_lab=Label(root,text=f'Time Left: {time_left}',textvariable=time_left_data,font=('Arail',20,'bold'))
point_label=Label(root,text=f'Point: {point}',textvariable=point_data,font=('Arail',20,'bold'))
time_left_data.set(f'Time Left: {time_left}')
point_data.set(f'Point: {point}')
colours=['Blue','Black','Red','Pink','Yellow','Grey','White','Brown','Cyan','Green','Purple',]
def time_left_func():
	global time_left
	global check
	global point
	check=False
	time_left-=1
	id=root.after(1000,time_left_func)
	time_left_data.set(f'Time Left: {time_left}')
	if time_left==0:
		root.after_cancel(id)
		QUEs=messagebox.askquestion('QUESTION',f'Times Up!! Your Point Are {point} Do You Want To Play Again?')
		if QUEs=='yes':
			input_.delete(0,END)
			time_left+=60
			time_left_data.set(f'Time Left: {time_left}')
			root.after(1000,time_left_func)
			point-=point
			point_data.set(f'Point: {point}')
		if QUEs=='no':
			root.unbind("<Return>")
			root.destroy()
def add_point(event):
	global point
	global check
	if (colour_label['fg']).lower()==input_.get().lower():
		point+=1
		point_data.set(f'Point: {point}')
		pygame.mixer.music.load('Good Job!.mp3')
		pygame.mixer.music.play()
	if (colour_label['fg']).lower()!=input_.get().lower():
		pygame.mixer.music.load('bruh.mp3')
		pygame.mixer.music.play()
	guide.place(x=4393)
	time_left_lab.place(x=375,y=35)
	point_label.place(x=415,y=75)
	colour_label.config(text=random.choice(colours))
	colour_label.config(fg=random.choice(colours))
	if check==True:
		time_left_func()
	input_.delete(0,END)
root.title('Colour Game!')
heAd=Label(root,text='Tip:Type in the colour of the words and do not type the text',font=('Arail',15,'bold')).pack()
guide=Label(root,text='Press Enter To Start The Game!!',font=('Arail',15,'bold'))
guide.pack()
input_=Entry(root,font=('Arail',17,'bold'),width=20)
input_.place(x=125,y=160)
colour_label=Label(root,text='',font=('Arial Rounded MT Bold',55,'bold'))
colour_label.place(x=136,y=45)
root.bind('<Return>',add_point)
mainloop()
# remove calling support in reminder app.
# check age calculator is giving accurate age.......
# count down soud effect if the point is less then 10!!!
# like 1,2,3,4,5,6,7,8,9,10!!
# how does a game is enjoable....
# check tommorw.