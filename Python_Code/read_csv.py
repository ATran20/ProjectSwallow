import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-pastel')

filepath = (r"C:\Users\ngaij\Desktop\Project Swallow Software\Python\Accelerometer\Set1.csv")
cols_list = ['Microphone1','X_Axis', 'Y_Axis', 'Z_Axis', 'Microphone2','Button']

def animate(i):
    df = pd.read_csv(filepath, header=None).drop_duplicates()
    df.columns = df.iloc[0]
    df = df.iloc[1:]

    M1 = df["Microphone1"].astype(float)
    X = df["X_Axis"].astype(float)
    Y = df["Y_Axis"].astype(float)
    Z = df["Z_Axis"].astype(float)
    M2 = df["Microphone2"].astype(float)
    btn = df["Button"].astype(float)

    plt.cla()
    plt.plot(M1, label="X-Axis")
    plt.plot(M2, label="Y-Axis")

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1)

plt.tight_layout()
plt.show()

# fig, ax=plt.subplots()
# ax.set_xlim(0,105)
# ax.set_ylim(0,1000)
# line, = ax.plot(0,0)
#
# def animation_frame(i):
#     X.append(i, *10)
#     time.append(i)
#
#     line.set_xdata(X)
#     line.set_ydata(time)
#     return line,
#
# animation = FuncAnimation(fig, func = animation_frame, frames= , interval=10)
# plt.show()


# plt.plot(X)
# plt.xlabel('Time')
# plt.ylabel('Value')
# plt.show()
