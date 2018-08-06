class InitSettings:

    stepdownDelay = 0.175  # Delay for beep during vibration/recovery state.

    numberOfSteps = 80  # tempo of steps per minute.

    laserToggle = True  # Whether laser turns on or off during recovery state.

    # Duration of the warning state between walking and recovering states. Time
    # is in seconds.
    vibrationState_Duration = 3

    # Entry delay before entry into respective states. The smaller the number,
    # the more responsive the system is. However, if the system is too
    # responsive, button responses may carry over between states and cause
    # errors. Time is in seconds.
    vibrationState_entryDelay = 0.5
    walkingState_entryDelay = 0.5
    pausedState_entryDelay = 3

    # Duration the "walking" is checked for. The smaller the number, the faster
    # the responsiveness of the system. The larger the number, the more
    # accurate the reading. For a good estimate of the "responsiveness" of the
    # system, multiply checkDuration by 3 (i.e. default is 2, so system should
    # respond within 6 seconds).
    checkDuration = 2

    # Duration of the startup sequence of the system. Important, as the button
    # has to be pressed during startup if one wants to enter data entry mode.
    # Time is in seconds.
    startupDuration = 5

    # Option to enable a secondary haptic pin or not. If True, a secondary pin
    # will be assigned via the secondHapticPin variable. Note that the
    # assignment of the secondary haptic pin is according to the BCM denotation,
    # not via the physical pin number (i.e. by default, the secondary haptic is
    # located in physical pin 36, which is known as BCM pin 16. Therefore, the
    # number assigned to secondaryPinHaptic is 16).
    enableSecondHaptic = False
    secondaryHapticPin = 16
