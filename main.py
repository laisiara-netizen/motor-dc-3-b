def on_logo_pressed():
    robotbit.motor_run_dual(robotbit.Motors.M1A, 150, robotbit.Motors.M2A, 150)
    basic.show_arrow(ArrowNames.NORTH)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    robotbit.motor_run_dual(robotbit.Motors.M1A, 150, robotbit.Motors.M2A, 0)
    basic.show_arrow(ArrowNames.WEST)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    robotbit.motor_run_dual(robotbit.Motors.M1A, -150, robotbit.Motors.M2A, -150)
    basic.show_arrow(ArrowNames.SOUTH)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_ab():
    robotbit.motor_stop_all()
    basic.clear_screen()
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    robotbit.motor_run_dual(robotbit.Motors.M1A, 0, robotbit.Motors.M2A, 150)
    basic.show_arrow(ArrowNames.EAST)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.CHESSBOARD)