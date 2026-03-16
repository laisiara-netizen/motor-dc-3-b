input.onButtonPressed(Button.A, function () {
    robotbit.MotorRunDual(
    robotbit.Motors.M1A,
    150,
    robotbit.Motors.M2A,
    0
    )
    basic.showArrow(ArrowNames.West)
})
input.onGesture(Gesture.LogoUp, function () {
    robotbit.MotorRunDual(
    robotbit.Motors.M1A,
    -150,
    robotbit.Motors.M2A,
    -150
    )
    basic.showArrow(ArrowNames.South)
})
input.onButtonPressed(Button.AB, function () {
    robotbit.MotorStopAll()
    basic.clearScreen()
    basic.showIcon(IconNames.Heart)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    robotbit.MotorRunDual(
    robotbit.Motors.M1A,
    150,
    robotbit.Motors.M2A,
    150
    )
    basic.showArrow(ArrowNames.North)
})
input.onButtonPressed(Button.B, function () {
    robotbit.MotorRunDual(
    robotbit.Motors.M1A,
    0,
    robotbit.Motors.M2A,
    150
    )
    basic.showArrow(ArrowNames.East)
})
basic.showIcon(IconNames.Chessboard)
