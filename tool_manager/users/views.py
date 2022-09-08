from tkinter import END, VERTICAL, StringVar, ttk

from tool_manager.color_map import color_map
from tool_manager.users.services import Services


def users_page(frame_master):
    global name, cpf, shift, phone, team, search_content

    services = Services()

    style = ttk.Style()
    style.configure('MainPageUsers.TFrame', background=color_map['background_central'])

    frame_page_users = ttk.Frame(frame_master, style='MainPageUsers.TFrame')
    frame_page_users.grid_rowconfigure(0, weight=1)
    frame_page_users.grid_columnconfigure(0, weight=1)

    frame_page_users.grid(row=0, column=0, sticky='ewns')

    # RESULTS TABLE
    label_frame_user_list = ttk.LabelFrame(frame_page_users, text='Listar')
    label_frame_user_list.grid(row=0, column=0, padx=8, pady=8, sticky='ewns')

    columns = ('name', 'cpf', 'shift', 'phone', 'team')

    results_table = ttk.Treeview(label_frame_user_list, columns=columns, show='headings')
    results_table.heading('name', text='Nome')
    results_table.heading('cpf', text='CPF')
    results_table.heading('phone', text='Telefone / Celular / Rádio')
    results_table.heading('shift', text='Turno')
    results_table.heading('team', text='Nome da Equipe')

    def select_item(a):
        current_item = results_table.focus()
        values = results_table.item(current_item)['values']
        name.set(values[0])
        cpf.set(values[1])
        shift.set(values[2])
        phone.set(values[3])
        team.set(values[4])

    results_table.bind('<ButtonRelease-1>', select_item)

    users = services.get_users()

    for user in users:
        results_table.insert('', END, values=user)

    results_table.grid(row=0, column=0, padx=6, pady=6, sticky='n')

    scrollbar = ttk.Scrollbar(label_frame_user_list, orient=VERTICAL, command=results_table.yview)
    results_table.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    # SEARCH/FILTER
    label_frame_search = ttk.LabelFrame(frame_page_users, text='Filtrar')
    label_frame_search.grid(row=1, column=0, padx=8, pady=8, sticky='ew')

    def filter_tree_view(tree, search_content):
        ids = tree.get_children()

        for id in ids:
            values = tree.item(id)['values']
            values = ', '.join(map(str, values))

            if search_content not in values:
                tree.delete(id)

    button_search = ttk.Button(
        label_frame_search,
        text='Filtrar',
        command=lambda: filter_tree_view(tree=results_table, search_content=search_content.get()),
    )
    button_search.grid(row=0, column=0, padx=10, pady=20)

    button_clear = ttk.Button(label_frame_search, text='Remover Filtro', command=lambda: users_page(frame_master))
    button_clear.grid(row=0, column=1, padx=10, pady=20)

    search_content = StringVar()
    textbox = ttk.Entry(label_frame_search, textvariable=search_content)
    textbox.grid(row=0, column=2, padx=10, pady=20)

    # EDIT DATA
    label_frame_edit = ttk.LabelFrame(frame_page_users, text='Editar')
    label_frame_edit.grid(row=2, column=0, padx=8, pady=8, sticky='ew')

    label = ttk.Label(
        label_frame_edit,
        text='Nome',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=0, column=0, padx=10, pady=20, sticky='w')

    name = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=name)
    textbox.grid(row=0, column=1)

    label = ttk.Label(
        label_frame_edit,
        text='CPF',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=0, column=2)

    cpf = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=cpf)
    textbox.grid(row=0, column=3, padx=10)

    label = ttk.Label(
        label_frame_edit,
        text='Telefone / Celular / Rádio',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=0, column=4, padx=10)

    phone = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=phone)
    textbox.grid(row=0, column=5)

    label = ttk.Label(
        label_frame_edit,
        text='Turno',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=1, column=0, padx=10, pady=20, sticky='w')

    shift = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=shift)
    textbox.grid(row=1, column=1)

    label = ttk.Label(
        label_frame_edit,
        text='Nome da Equipe',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=1, column=2, padx=10)

    team = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=team)
    textbox.grid(row=1, column=3)

    button_add = ttk.Button(
        label_frame_edit,
        text='Adicionar',
        command=lambda: [
            services.create_user(name=name.get(), cpf=cpf.get(), shift=shift.get(), phone=phone.get(), team=team.get()),
            users_page(frame_master),
        ],
    )
    button_add.grid(row=2, column=0, padx=10, pady=20)

    button_update = ttk.Button(
        label_frame_edit,
        text='Atualizar',
        command=lambda: [
            services.update_user(name=name.get(), cpf=cpf.get(), shift=shift.get(), phone=phone.get(), team=team.get()),
            users_page(frame_master),
        ],
    )
    button_update.grid(row=2, column=1, padx=10, pady=20)

    button_delete = ttk.Button(
        label_frame_edit,
        text='Excluir',
        command=lambda: [services.delete_user(cpf=cpf.get()), users_page(frame_master)],
    )
    button_delete.grid(row=2, column=2, padx=10, pady=20)

    button_clear = ttk.Button(
        label_frame_edit,
        text='Limpar Campos',
        command=lambda: users_page(frame_master),
    )
    button_clear.grid(row=2, column=3, padx=10, pady=20)
