from tkinter import Tk, Label
import asynctkinter as at
at.patch_unbind()

def heavy_task():
    import time
    for i in range(5):
        time.sleep(1)
        print('heavy task:', i)

root = Tk()
label = Label(root, text='Hello', font=('', 60))
label.pack()

async def some_task(label):
    label['text'] = 'start heavy task'
    event = await at.event(label, '<Button>')
    label['text'] = 'running...'
    await at.thread(heavy_task, sleep_by=label)
    label['text'] = 'done'
    await at.sleep(label, 2000)
    label['text'] = 'close the window'


at.start(some_task(label))
root.mainloop()