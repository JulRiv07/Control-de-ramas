meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "67": "No se",
            "AURA": "Tener buena vibra",
            "GHOSTEAR": "Ignorar a alguien",
            "FUNA": "Criticar o atacar a alguien",
            "STALKEAR": "Revisar la informacion de alguien",
            "ROFL" : "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }

while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(word, "significa: ", meme_dict[word])
    else:
        print("Ni yo lo sé, pero prueba poniendolo en mayusculas")
        break
