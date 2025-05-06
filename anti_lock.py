import pyautogui
import time

def prevent_lock(interval_seconds=60):
    print(f"Démarrage de l'anti-verrouillage... (Ctrl+C pour arrêter)")
    try:
        while True:
            x, y = pyautogui.position()
            pyautogui.moveTo(x + 1, y + 1, duration=0.1)
            pyautogui.moveTo(x, y, duration=0.1)
            print("Mouvement simulé 🖱️")
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("Arrêt du script.")

if __name__ == "__main__":
    prevent_lock()
