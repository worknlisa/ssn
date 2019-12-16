
from random import randint
import tkinter as tk


def valid_ssn(ssn):
	'''
	Checks to see if the input (ssn) matches criteria to be a valid SSN .    
	'''

	if type(ssn) != str:
		return False
	elif len(ssn) != 9:
		return False
	elif ssn[0] == '9':
		return False
	elif ssn[:3] == '666':
		return False
	elif ssn[:3] == '000':
		return False
	elif ssn[3:5] == '00':
		return False
	elif ssn[5:] == '0000':
		return False
	else:
		return True


def generate_ssn(event):
	'''
	Generates a string of nine random digits and checks to see if qualifies as a valid SSN.
	'''
	
	generate = True
	while generate:
	
		lista = [randint(0,9) for n in range(9)]
		ssn = ''.join(map(str,lista))
	
		if valid_ssn(ssn):
			generate = False
			ssn = ssn[:3] + '-' + ssn[3:5] + '-' + ssn[5:]
			output.config(text=ssn) # tkinter output 
		else:
			pass

# tkinter code

win = tk.Tk()
win.title('ssn g3n3r4t0r!!!')
win.config(bg='black')

button = tk.Button(win, text='Generate!', highlightbackground='black', bg='black', fg='#39ff14')
button.bind('<Button-1>', generate_ssn)
button.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

output = tk.Label(win, text='', fg='red', bg='black')
output.place(relx=0.5, rely=.65, anchor=tk.CENTER)


# Centering window

w = 200
h = 100

ws = win.winfo_screenwidth()
hs = win.winfo_screenheight()

x = int(ws/2 - w/2)
y = int(hs/2 - h/2)

win.geometry('%dx%d+%d+%d' % (w,h,x,y))


if __name__ == '__main__':
	win.mainloop()
