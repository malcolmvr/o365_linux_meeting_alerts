from os import getenv, system

def show_imminent_event(was_imminent: bool, is_imminent: bool):
    color = getenv('IMMINENT_DESKTOP_BACKGROUND_COLOR') if is_imminent else getenv('NORMAL_DESKTOP_BACKGROUND_COLOR')
    system(f"gsettings set org.gnome.desktop.background primary-color '#{color}'")
    if was_imminent != is_imminent:
        system(f"ffplay -autoexit -nodisp -volume 30 alarm.mp3")
