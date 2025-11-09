import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox


def update(val):
    try:
        angle_deg = float(val)  
    except ValueError:
        return  
    angle_rad = np.radians(angle_deg)  

    
    sin_val = np.sin(angle_rad)
    cos_val = np.cos(angle_rad)

    
    ax.cla()

    circle = plt.Circle((0, 0), 1, color='lightblue', fill=True, alpha=0.5)
    ax.add_artist(circle)

   
    ax.axhline(0, color='black',linewidth=1)  # x-axis
    ax.axvline(0, color='black',linewidth=1)  # y-axis

    
    ax.plot([0, cos_val], [0, sin_val], color='black', lw=2)  
    ax.plot([0, cos_val], [0, 0], color='black', lw=2)  
    ax.plot([cos_val, cos_val], [0, sin_val], color='black', lw=2) 

    
    ax.fill([0, cos_val, cos_val], [0, 0, sin_val], color='orange', alpha=0.3)

    
    ax.scatter(cos_val, sin_val, color='red', zorder=5)  

    
    if angle_deg > 0:
        ax.text(0.1, 0.05, f'{angle_deg:.0f}°', fontsize=12, color='darkgreen', ha='center')

    
    ax.text(cos_val / 2, -0.05, f'cos = {cos_val:.2f}', ha='center', fontsize=12, color='blue')

    
    ax.text(cos_val + 0.05, sin_val / 2, f'sin = {sin_val:.2f}', va='center', fontsize=12, color='red')

   
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_xlabel('cos')
    ax.set_ylabel('sin')
    ax.set_title('Unit Circle with sin and cos values')

    
    plt.draw()


fig, ax = plt.subplots(figsize=(6,6))
ax.set_xticks(np.linspace(-1, 1, 5))
ax.set_yticks(np.linspace(-1, 1, 5))
ax.grid(True)


ax_slider = plt.axes([0.1, 0.02, 0.8, 0.05], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, 'Angle (°)', 0, 360, valinit=0, valstep=1)


ax_textbox = plt.axes([0.1, 0.1, 0.8, 0.05], facecolor='lightgoldenrodyellow')
text_box = TextBox(ax_textbox, 'Input Angle (°)', initial='0')


slider.on_changed(lambda val: update(val))
text_box.on_submit(update)


update(0)

plt.show()