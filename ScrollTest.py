import pynput
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# adapted from
# https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/update-a-graph-in-real-time

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ys = [0]*100

# https://pypi.org/project/pynput/
  
def on_scroll(x, y, dx, dy):
  ys.append(dy)

listener = pynput.mouse.Listener(
  on_scroll=on_scroll
)

listener.start()

def animate(i, ys, an):
  ax.clear()
  ys = ys[-100:]
  ax.plot(ys)
  plt.axhline(y=0, color='r', linestyle='-')
  plt.xticks([])
  plt.subplots_adjust(bottom=0.5)
  plt.title('Mapping Vert. Scroll Input...')
  
ani = animation.FuncAnimation(fig, animate, fargs=(ys, 0), interval=(10))

plt.show()