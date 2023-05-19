import math

def get_rainbow_color(time):
    # Define the rainbow colors
    colors = [(255, 0, 0), (255, 65, 0), (255, 255, 0), (0, 255, 0),
              (0, 0, 255), (29, 0, 51), (155,38,182), (255, 0, 0)]

    # Calculate the color offset based on time
    color_offset = time % 1  # Normalize time within [0, 1]

    # Calculate the index of the current color
    color_index = int(color_offset * (len(colors) - 1))

    # Calculate the interpolation factor between the current and next color
    interp_factor = color_offset * (len(colors) - 1) % 1

    # Get the current and next colors
    current_color = colors[color_index]
    next_color = colors[(color_index + 1) % len(colors)]

    # Interpolate between the current and next colors
    interpolated_color = lerp(current_color, next_color, interp_factor)
    
    return interpolated_color


def lerp(color1, color2, t):
    r = int(color1[0] * (1 - t) + color2[0] * t)
    g = int(color1[1] * (1 - t) + color2[1] * t)
    b = int(color1[2] * (1 - t) + color2[2] * t)
    return (r, g, b)
