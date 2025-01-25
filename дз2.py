import colorama
import inspect

print(inspect.getmembers(colorama))

colorama.init()

print(colorama.Fore.RED + "Цей текст буде червоним!")
print(colorama.Fore.GREEN + "Цей текст буде зеленим!")

print(colorama.Back.YELLOW + "Текст з жовтим фоном!")

print(colorama.Style.BRIGHT + "Цей текст буде яскравим!")
print(colorama.Style.NORMAL + "Цей текст буде нормального стилю.")

colorama.deinit()