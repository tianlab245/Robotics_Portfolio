# Setup: Color Sensor on port E, facing the fruit.
# Force Sensor on port A switches from training to inference.
# Hold the Color Sensor at about the same distance for training and scanning.

from hub import port, button, sound, light_matrix
import runloop
import color_sensor
import force_sensor

APPLE_SOUND_HZ = 440
BANANA_SOUND_HZ = 660
SOUND_LENGTH_MS = 200

async def main():
    # Each example stores red, green, blue, and its fruit name.
    examples = []

    ##### Training #####
    print("Training: left = apple, right = banana")
    print("Press the Force Sensor to finish training")

    while True:
        # The Force Sensor ends training once at least 3 examples are saved.
        if force_sensor.pressed(port.A):
            if len(examples) >= 3:
                break
            print("Save at least 3 examples first.")

            # Wait for release so this warning appears only once per press.
            while force_sensor.pressed(port.A):
                await runloop.sleep_ms(10)

        elif button.pressed(button.LEFT):
            # Save the current color reading as an apple.
            red, green, blue, intensity = color_sensor.rgbi(port.E)
            examples.append((red, green, blue, "apple"))
            print("Saved apple:", red, green, blue)
            await sound.beep(APPLE_SOUND_HZ, SOUND_LENGTH_MS)

            # Wait for release so one press saves only one example.
            while button.pressed(button.LEFT):
                await runloop.sleep_ms(10)

        elif button.pressed(button.RIGHT):
            # Save the current color reading as a banana.
            red, green, blue, intensity = color_sensor.rgbi(port.E)
            examples.append((red, green, blue, "banana"))
            print("Saved banana:", red, green, blue)
            await sound.beep(BANANA_SOUND_HZ, SOUND_LENGTH_MS)

            # Wait for release so one press saves only one example.
            while button.pressed(button.RIGHT):
                await runloop.sleep_ms(10)

        await runloop.sleep_ms(10)

    ##### Inference #####
    print("Inference: press right to scan")

    # Wait for the Force Sensor to be released after switching modes.
    while force_sensor.pressed(port.A):
        await runloop.sleep_ms(10)

    while True:
        if button.pressed(button.RIGHT):
            # Read the object as a point in red-green-blue space.
            red, green, blue, intensity = color_sensor.rgbi(port.E)

            # Find the squared 3D distance to every saved example.
            # Squared distances preserve which examples are nearest.
            distances = []
            for example in examples:
                red_difference = red - example[0]
                green_difference = green - example[1]
                blue_difference = blue - example[2]

                distance = (
                    red_difference * red_difference
                    + green_difference * green_difference
                    + blue_difference * blue_difference
                )
                distances.append((distance, example[3]))

            # Put the nearest saved examples first.
            distances.sort()

            # The 3 nearest examples vote on the result.
            apple_votes = 0
            banana_votes = 0
            for neighbor_number in range(3):
                if distances[neighbor_number][1] == "apple":
                    apple_votes += 1
                else:
                    banana_votes += 1

            # Display the winning fruit and play its sound.
            if apple_votes > banana_votes:
                await light_matrix.write("APPLE")
                await sound.beep(APPLE_SOUND_HZ, SOUND_LENGTH_MS)
            else:
                await light_matrix.write("BANANA")
                await sound.beep(BANANA_SOUND_HZ, SOUND_LENGTH_MS)

            # Wait for release so one press performs only one scan.
            while button.pressed(button.RIGHT):
                await runloop.sleep_ms(10)

        await runloop.sleep_ms(10)

runloop.run(main())
