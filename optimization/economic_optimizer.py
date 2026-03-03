def optimize_rpm(vibration):

    if vibration > 1.5:
        return 1100
    elif vibration > 1:
        return 1400
    else:
        return 1800