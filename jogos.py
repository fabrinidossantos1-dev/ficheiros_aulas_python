import random

# Status iniciais dos personagens
heroi_vida = 100
monstro_vida = 100

turno = 1

print("=== A BATALHA COMEÇOU! ===")
print(f"Herói: {heroi_vida} HP | Monstro: {monstro_vida} HP\n")

# O loop continua enquanto ambos estiverem vivos
while heroi_vida > 0 and monstro_vida > 0:
    print(f"--- Turno {turno} ---")
    
    # Alterna os turnos usando o resto da divisão (%)
    # Turnos pares (0): Herói ataca; Turnos ímpares (1): Monstro ataca
    if turno % 2 == 0:
        # Vez do Monstro
        dano_monstro = random.randint(10, 25)
        heroi_vida -= dano_monstro
        # Garante que a vida não fique negativa
        if heroi_vida < 0:
            heroi_vida = 0
        print(f"O Monstro atacou e causou {dano_monstro} de dano!")
        print(f"Vida restante do Herói: {heroi_vida} HP")
    else:
        # Vez do Herói
        dano_heroi = random.randint(12, 28)
        monstro_vida -= dano_heroi
        if monstro_vida < 0:
            monstro_vida = 0
        print(f"Você atacou o Monstro e causou {dano_heroi} de dano!")
        print(f"Vida restante do Monstro: {monstro_vida} HP")
        
    print("-" * 25)
    turno += min(1, 1) # ou apenas turno += 1

# Verificando quem venceu
print("\n=== FIM DE JOGO ===")
if heroi_vida > 0:
    print("Parabéns! Você derrotou o monstro e venceu a batalha! 🎉")
else:
    print("Você foi derrotado pelo monstro... Tente novamente! 💀")
