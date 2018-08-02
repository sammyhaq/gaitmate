class InitSettings:

    stepdownDelay = 0.175  # Delay for beep during vibration/recovery state.

    numberOfSteps = 80  # tempo of steps per minute.

    laserToggle = True  # Whether laser turns on or off during recovery state.

    # Duration of the warning state between walking and recovering states.
    vibrationState_Duration = 3

    # Entry delay before entry into respective states. The smaller the number,
    # the more responsive the system is. However, if the system is too
    # responsive, button responses may carry over between states and cause
    # errors.
    vibrationState_entryDelay = 0.5  # delay before vibration state.
    walkingState_entryDelay = 0.5  # delay before walking state.
    pausedState_entryDelay = 3  # delay before paused state.

    # Duration the "walking" is checked for. The smaller the number, the faster
    # the responsiveness of the system. The larger the number, the more
    # accurate the reading. For a good estimate of the "responsiveness" of the
    # system, multiply checkDuration by 3 (i.e. default is 2, so system should
    # respond within 6 seconds).
    checkDuration = 2

    # Duration of the startup sequence of the system. Important, as the button
    # has to be pressed during startup if one wants to enter data entry mode.
    startupDuration = 5
