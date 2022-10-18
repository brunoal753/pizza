from PySimpleGUI import PySimpleGUI as s


# Layouts
def janela_login():
    s.theme('Reddit')
    layout = [
        [s.Text('Qual seu nome?')],
        [s.Input()],
        [s.Button('Continuar')]
    ]
    return s.Window('Login', layout=layout, finalize=True)


def janela_pedido():
    s.theme('Reddit')
    layout = [
        [s.Text('Fazer Pedido')],
        [s.Checkbox('Pizza Pepperoni', key='pizza1')],
        [s.Checkbox('Pizza  4 Queijos', key='pizza2')],
        [s.Button('Voltar'), s.Button('Fazer Pedido')]
    ]
    return s.Window('Montar Pedido', layout=layout, finalize=True)


# Janelas iniciais
janela1, janela2 = janela_login(), None

# Loop  de leitura de eventos
while True:
    window, event, values = s.read_all_windows()
    # Quando janela for fechada
    if window == janela1 and event == s.WIN_CLOSED:
        break

    # Quando queremos ir para próxima janela
    if window == janela1 and event == 'Continuar':
        janela1.hide()
        janela2 = janela_pedido()

    if window == janela2 and event == 'Voltar':
        janela2.hide()            
        janela1.un_hide()  

    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            s.popup('Foram solicitados uma Pizza Pepperoni e uma Pizza 4 Queijos.')
        elif values['pizza1'] == True:
            s.popup('Foi solicitado uma Pizza Peperoni')
        elif values['pizza2'] == True:
            s.popup('Foi solicitado uma Pizza 4 Queijos')