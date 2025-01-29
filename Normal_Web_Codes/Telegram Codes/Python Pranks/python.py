import ctypes

def rotate_screen(rotation):
    DMDO_DEFAULT = 0
    DMDO_90 = 1
    DMDO_180 = 2
    DMDO_270 = 3

    user32 = ctypes.windll.user32
    user32.ChangeDisplaySettingsExW(None, None, None, 0, None)
    user32.ChangeDisplaySettingsExW(None, None, None, DMDO_DEFAULT, None)
    user32.ChangeDisplaySettingsExW(None, None, None, rotation, None)

if __name__ == "__main__":
    rotate_screen(DMDO_DEFAULT)  # You can change the rotation value as needed
