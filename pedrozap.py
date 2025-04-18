#criar chat
#framework - pacote de codigo que é necessário seguir as regras para utiliza-lo
#visual (frontend) / logica (backend)
#TITULO> CHAT DA LUA E DO SOL

#botao: Iniciar CHat
    #quando eu clicar no botao:
    #janela / dialog / modal / popup
    #titulo: BEM VINDO 
    #botao: ENTRAR NO CHAT
    #fechar o dialog
        #criar o chat
        #criar o campo de mensagem 
        #botao: ENVIAR
            #quando clicar no botão:
            #envie a mensagem para o chat

#importar flet
import flet as ft

#criar a função principal (main) do aplicativo
def main(page):
    #criar elementos
    titulo = ft.Text("CHAT DO PEDRINHO")
    titulo_janela = ft.Text("Bem vindo ao Chat")

    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem) #valor do campo mensagem
        chat.controls.append(texto_mensagem)
        page.update()

    #websocket - tunel de comunicação 
    page.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        mensagem = f"{campo_nome.value}: {campo_mensagem.value}"#valor do campo mensagem
        #enviar a mensagem no tunel
        page.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        page.update()


    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    #arquivo = ft.FilePicker() pede pro usuario fazer upload de arquivos


    chat = ft.Column()
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        page.pubsub.send_all(f"{campo_nome.value} entrou no chat")
        #fechar a janela / dialog
        janela.open = False

        #tirar o titulo e botao_iniciar
        page.remove(titulo)
        page.remove(botao_iniciar)
        

        #criar o chat
        page.add(chat)

        #botao enviar
        page.add(linha_mensagem)
        page.update()

    campo_nome = ft.TextField(label="Digite o seu nome", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela,
        content=campo_nome,
        actions=[botao_entrar]
    )
    
    

    def abrir_dialog(evento):
        page.dialog = janela
        page.open(janela)
        page.update()

    

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_dialog) #executar o que está na função ao clicar no butao


    # colocar os elementos na pagina
    page.add(titulo)
    page.add(botao_iniciar)

#rodar o seu aplicativo
ft.app(main, view=ft.WEB_BROWSER)


#sempre que voce clica em qualquer botao - o flet cria um evento