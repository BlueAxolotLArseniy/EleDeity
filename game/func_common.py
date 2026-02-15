import ctypes

def get_screen_resolution() -> tuple[float, float]:
    ctypes.windll.user32.SetProcessDPIAware()
    width = ctypes.windll.user32.GetSystemMetrics(0)
    height = ctypes.windll.user32.GetSystemMetrics(1)
    return width, height

def get_screen_specs():
    """
    Возвращает реальное разрешение экрана и коэффициент масштабирования (Scale).
    """
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        ctypes.windll.user32.SetProcessDPIAware()

    user32 = ctypes.windll.user32
    gdi32 = ctypes.windll.gdi32

    physical_width = user32.GetSystemMetrics(0)
    physical_height = user32.GetSystemMetrics(1)

    hdc = user32.GetDC(0)
    dpi = gdi32.GetDeviceCaps(hdc, 88)
    user32.ReleaseDC(0, hdc)

    scale = dpi / 96.0

    return physical_width, physical_height, scale