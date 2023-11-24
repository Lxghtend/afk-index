
import pyautogui
import asyncio
import keyboard
import random2
extract = 'extract.png'
async def main():
    rounds = 1
    while True:
        if await pyautogui.locateCenterOnScreen(extract, confidence=0.5):
            print(f"The extract menu is availible! {rounds} Round{'' if rounds == 1 else 's'} done!")
            rounds += 1
            await asyncio.sleep(16)
            continue
        print(f'Exiting and re-entering operator form...')
        print(f"{rounds} Round{'' if rounds == 1 else 's'} done!")
        keyboard.press_and_release('5')
        await asyncio.sleep(random2.randint(1, 2))
        keyboard.press_and_release('5')
        
        await asyncio.sleep(10) 

asyncio.run(main())