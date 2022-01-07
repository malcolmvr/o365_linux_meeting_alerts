import os

def show_imminent_event(is_imminent: bool):
    color = '#ff0000' if is_imminent else '#222222'
    print("color=", color)
    os.system(f"gsettings set org.gnome.desktop.background primary-color '{color}'")
