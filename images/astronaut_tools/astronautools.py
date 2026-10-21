# Start your new code here!
# Setup: force sensor on port B, motor on port D.
# Left hub button selects clockwise; right selects anticlockwise.

from hub import port, button, light_matrix, sound
import runloop
import motor
import force_sensor

MOTOR_SPEED = 800  # Faster speed in degrees per second.

async def main():
    # Start stopped, with no direction selected.
    direction = 0
    shown_direction = 0
    await light_matrix.write("X")

    while True:
        # Select a direction with a hub button.
        if button.pressed(button.LEFT):
            direction = 1
        elif button.pressed(button.RIGHT):
            direction = -1

        # Run only while the force sensor is pressed.
        if force_sensor.pressed(port.B) and direction != 0:
            if direction == 1:
                motor.run(port.D, MOTOR_SPEED)

                # Clockwise shows the down arrow.
                if shown_direction != 1:
                    light_matrix.show_image(light_matrix.IMAGE_ARROW_S)
                    shown_direction = 1
                    await sound.beep(880, 120, 100)
            else:
                motor.run(port.D, -MOTOR_SPEED)

                # Anticlockwise shows the up arrow.
                if shown_direction != -1:
                    light_matrix.show_image(light_matrix.IMAGE_ARROW_N)
                    shown_direction = -1
                    await sound.beep(440, 120, 100)
        else:
            # Stop the motor and show X when it is not turning.
            motor.stop(port.D)
            if shown_direction != 0:
                await light_matrix.write("X")
                shown_direction = 0

        # Pause briefly before checking the controls again.
        await runloop.sleep_ms(20)

runloop.run(main())
