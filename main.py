def sistema_ada():
    nome_bot= "Ada"
    print ("---------------------------------------------------------")
    print (f"👩‍💻 {nome_bot} Inicializada...")
    print (f"{nome_bot}: Olá! Sou a {nome_bot}, sua assistente virtual de T.I")
    print ("Estou pronta para ajudar. Me diga o que está acontecendo.")
    print ("---------------------------------------------------------")

    while True:
        texto_usuario = input("\nVocê: ").lower()
        if "sair" in texto_usuario or "encerrar" in texto_usuario:
            print (f"{nome_bot}: Encerrando sessão. Conte comigo sempre que precisar!")
            break
        elif "internet" in texto_usuario or "wifi" in texto_usuario:
            print (f"{nome_bot}: Vamos tentar reiniciar o roteador. Desconecte-o da tomada, aguarde 30 segundos e conecte novamente.")
        elif "impressora" in texto_usuario:
            print (f"{nome_bot}: Entendi, problemas de impressão são comuns mesmo.")
            print (f"{nome_bot}: Verifique se a impressora está ligada e conectada corretamente ao computador. Tente retirar e inserir o cabo novamente e reiniciar ambos os dispositivos.")
        elif "senha" in texto_usuario or "login" in texto_usuario:
            print (f"{nome_bot}: Esqueceu a senha, quem nunca?")
            print (f"{nome_bot}: Entre no link 'esqueceu-senha' no portal do funcionário para redefini-la.")
        elif "monitor" in texto_usuario or "tela" in texto_usuario:
            print (f"{nome_bot}: Pode ser um mau contato.")
            print (f"{nome_bot}: Mexa um pouco no cabo atrás do monitor para ver se a imagem volta. Se não funcionar, tente conectar outro monitor para identificar se o problema é do monitor ou do computador.")
        elif "computador lento" in texto_usuario or "desempenho" in texto_usuario:
            print (f"{nome_bot}: Computadores lentos podem ser frustrantes.")
            print (f"{nome_bot}: Tente fechar programas desnecessários e reiniciar o computador. Tente fazer uma limpeza de arquivos temporários e verifique se há programas iniciando junto com o sistema que possam estar consumindo muitos recursos.")
            print (f"{nome_bot}: Reinicie o computador após essas ações para ver se o desempenho melhora.")
            print (f"{nome_bot}: Se o problema persistir, pode ser necessário verificar se há vírus ou considerar um upgrade de hardware.")
        elif "obrigado" in texto_usuario or "valeu" in texto_usuario or "agradeço" in texto_usuario:
            print (f"{nome_bot}: De nada! Estou aqui para ajudar sempre que precisar.")
        elif "Deu certo" in texto_usuario or "resolveu" in texto_usuario:
            print (f"{nome_bot}: Fico feliz em saber que deu certo! Se precisar de mais ajuda, é só chamar.")

        #Sobre a Ada
        elif "quem é você" in texto_usuario or "o que você faz" in texto_usuario:
            print (f"{nome_bot}: Eu sou a {nome_bot}, uma assistente virtual desenvolvida para ajudar com problemas comuns de T.I.")
        elif "seu nome" in texto_usuario:
            print (f"{nome_bot}: Meu nome é {nome_bot}. Uma homenagem à matemática e escritora Ada Lovelace.")
            print (f"{nome_bot}:Ela foi a primeira programadora da história, no século 19!")
        
        else:
            print(f"{nome_bot}: Desculpe, ainda estou aprendendo.")
            print(f"{nome_bot}: Tente usar palavras simples como 'internet' ou 'senha'.")

if __name__ == "__main__":
    sistema_ada()