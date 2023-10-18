import random

generate_random_rgb = lambda: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

display_rgb = lambda rgb: print(f"RGB atual: {rgb}")

adjust_rgb = lambda rgb: (
    int(input(f"Insira o novo valor para o Red (atual: {rgb[0]}): ")),
    int(input(f"Insira o novo valor para o Green (atual: {rgb[1]}): ")),
    int(input(f"Insira o novo valor para o Blue (atual: {rgb[2]}): "))
)

actions = {
    'sim': lambda rgb: (display_rgb((new_rgb := adjust_rgb(rgb))), loop(new_rgb)),
    'não': lambda _: None,
    'default': lambda _: (print("Escolha inválida. Insira sim ou não"), loop(rgb))
}

loop = lambda rgb_val: actions.get(
    input("Você gostaria de ajustar os valores RGB? (sim/não): ").lower(),
    actions['default']
)(rgb_val)

rgb = generate_random_rgb()
display_rgb(rgb)
loop(rgb)