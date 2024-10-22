import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Reboiler_code

# Create figure for plotting
plt.style.use('fivethirtyeight')

real_time = []
ip = []
op= []

# Initialize communication with TMP102
#FOPTD_final.init()

# This function is called periodically from FuncAnimation
def animate(i):

    # Read temperature (Celsius) from TMP102
    temp_ip = Reboiler_code.xs[i]
    temp_op = Reboiler_code.ys[i]

    # Add x and y to lists
    real_time.append(dt.datetime.now().strftime('%M:%S'))
    ip.append(temp_ip)
    op.append(temp_op)

    # Limit x and y lists to 20 items
    #xs = xs[-20:]
    #ys = ys[-20:]

    # Draw x and y lists
    plt.cla()

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.plot(real_time, ip, label='Input func')
    plt.plot(real_time, op, label='Output response')
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()
