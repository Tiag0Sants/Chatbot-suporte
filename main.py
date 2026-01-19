def sistema_ada():
    nome_bot= "Ada"

    #Dicionário de respostas pré-definidas
    respostas = {
        ("internet", "wifi"): "Reinicie o modem e aguarde as luzes estabilizarem.",
        ("senha", "login"): "Você pode redefinir sua senha clicando em 'Esqueci minha senha' na tela de login.",
        ("impressora",): "Verifique se a impressora está ligada e conectada corretamente ao computador. Retire e reinsira os cabos, se necessário. Verfique também se há papel e tinta.",
        ("monitor", "tela"): "Pode ser um mau contato. Mexa um pouco no cabo atrás do monitor para ver se a imagem volta. \n Se não funcionar, tente conectar outro monitor para identificar se o problema é do monitor ou do computador.",
        ("computador lento", "desempenho"): "Computadores lentos podem ser frustrantes. Tente fechar programas desnecessários e reiniciar o computador. \n Tente fazer uma limpeza de arquivos temporários e verifique se há programas iniciando junto com o sistema que possam estar consumindo muitos recursos."
        "\n Reinicie o computador após essas ações para ver se o desempenho melhora. \n Se o problema persistir, pode ser necessário verificar se há vírus ou considerar um upgrade de hardware.",
        ("cafe",): "Desculpe, ainda não tenho corpo físico para buscar café! ☕",
        ("obrigado", "valeu", "agradeço"): "De nada! Estou aqui para ajudar sempre que precisar.",
        ("deu certo", "resolveu"):"Fico feliz em saber que deu certo! Se precisar de mais ajuda, é só chamar.",
        ("quem é você", "o que você faz"): "Sou a Ada, sua assistente virtual de T.I. Estou aqui para ajudar com problemas técnicos e fornecer suporte de T.I sempre que você precisar.",
        ("seu nome",): f"Meu nome é {nome_bot}. Uma homenagem à matemática e escritora Ada Lovelace."
        "\n Ela foi a primeira programadora da história, no século 19!"
        }


    print ("-" * 57)
    print (f"👩‍💻 {nome_bot} Inicializada...")
    print (f"{nome_bot}: Olá! Sou a {nome_bot}, sua assistente virtual de T.I")
    print ("Estou pronta para ajudar. Me diga o que está acontecendo.")
    print ("-" * 57)

    while True:
        texto_usuario = input("\n Você: ").lower()
        if "sair" in texto_usuario or "encerrar" in texto_usuario:
            print(f"{nome_bot}: Encerrando sessão. Conte comigo sempre que precisar!")
            break

        encontrei_resposta = False

        for palavras_chave, resposta in respostas.items():

            for palavra in palavras_chave:
                if palavra in texto_usuario:
                    print(f"{nome_bot}: {resposta}")
                    encontrei_resposta = True
                    break # Para de procurar assim que achar uma palavra que serve  

        if not encontrei_resposta:
            print(f"{nome_bot}: Desculpe, ainda estou aprendendo. Tente palavras como 'wifi', 'senha' ou 'impressora'.")

if __name__ == "__main__":
    sistema_ada()