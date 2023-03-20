def convert_byte(value):
    if value >= 1024 ** 4:
        return float(f"{value / (1024 ** 4): .2f}"), "TB"
    elif value >= 1024 ** 3:
        return float(f"{value/(1024**3): .2f}"), "GB"
    elif value >= 1024 ** 2:
        return float(f"{value / (1024 ** 2): .2f}"), "MB"
    elif value >= 1024:
        return float(f"{value / 1024: .2f}"), "KB"
    else:
        return value, "B"
