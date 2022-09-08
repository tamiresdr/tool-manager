from tkinter import END, HORIZONTAL, VERTICAL, StringVar, ttk

from tool_manager.color_map import color_map
from tool_manager.tools.services import Services


def tools_page(frame_master):
    global _id, description, manufacturer, voltage, part_number, size, unit_measurement, _type, material, max_reservation_time, search_content

    services = Services()

    style = ttk.Style()
    style.configure('MainPageTools.TFrame', background=color_map['background_central'])

    frame_page_tools = ttk.Frame(frame_master, style='MainPageTools.TFrame')
    frame_page_tools.grid_rowconfigure(0, weight=1)
    frame_page_tools.grid_columnconfigure(0, weight=1)

    frame_page_tools.grid(row=0, column=0, sticky='ewns')

    # RESULTS TABLE
    label_frame_tool_list = ttk.LabelFrame(frame_page_tools, text='Listar')
    label_frame_tool_list.grid(row=0, column=0, padx=8, pady=8, sticky='ewns')

    columns = (
        'id',
        'description',
        'manufacturer',
        'voltage',
        'part_number',
        'size',
        'unit_measurement',
        'type',
        'material',
        'max_reservation_time',
    )

    results_table = ttk.Treeview(label_frame_tool_list, columns=columns, show='headings')
    results_table.heading('id', text='ID da ferramenta')
    results_table.heading('description', text='Descrição da ferramenta')
    results_table.heading('manufacturer', text='Fabricante')
    results_table.heading('voltage', text='Voltagem de uso')
    results_table.heading('part_number', text='Part Number')
    results_table.heading('size', text='Tamanho')
    results_table.heading('unit_measurement', text='Unidade de medida')
    results_table.heading('type', text='Tipo de ferramenta')
    results_table.heading('material', text='Material da ferramenta')
    results_table.heading('max_reservation_time', text='Tempo máximo de reserva')

    def select_item(a):
        current_item = results_table.focus()
        values = results_table.item(current_item)['values']

        _id.set(values[0])
        description.set(values[1])
        manufacturer.set(values[2])
        voltage.set(values[3])
        part_number.set(values[4])
        size.set(values[5])
        unit_measurement.set(values[6])
        _type.set(values[7])
        material.set(values[8])
        max_reservation_time.set(values[9])

    results_table.bind('<ButtonRelease-1>', select_item)

    tools = services.get_tools()

    for tool in tools:
        results_table.insert('', END, values=tool)

    results_table.place(relx=0.01, rely=0.128, width=998, height=200)

    scrollbary = ttk.Scrollbar(label_frame_tool_list, orient=VERTICAL, command=results_table.yview)
    results_table.configure(yscroll=scrollbary.set)
    scrollbary.place(relx=0.984, rely=0.128, width=22, height=190)

    scrollbarx = ttk.Scrollbar(label_frame_tool_list, orient=HORIZONTAL, command=results_table.xview)
    results_table.configure(xscroll=scrollbarx.set)
    scrollbarx.place(relx=0.002, rely=0.922, width=1006, height=22)

    # SEARCH/FILTER
    label_frame_search = ttk.LabelFrame(frame_page_tools, text='Filtrar')
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

    button_clear = ttk.Button(label_frame_search, text='Remover Filtro', command=lambda: tools_page(frame_master))
    button_clear.grid(row=0, column=1, padx=10, pady=20)

    search_content = StringVar()
    textbox = ttk.Entry(label_frame_search, textvariable=search_content)
    textbox.grid(row=0, column=2, padx=10, pady=20)

    # EDIT DATA
    label_frame_edit = ttk.LabelFrame(frame_page_tools, text='Editar')
    label_frame_edit.grid(row=2, column=0, padx=8, pady=8, sticky='ew')

    label = ttk.Label(
        label_frame_edit,
        text='ID da ferramenta',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=0, column=0, padx=10, pady=20, sticky='w')

    _id = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=_id)
    textbox.grid(row=0, column=1)

    label = ttk.Label(
        label_frame_edit,
        text='Descrição da ferramenta',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=0, column=2, padx=10, pady=20, sticky='w')

    description = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=description)
    textbox.grid(row=0, column=3)

    label = ttk.Label(
        label_frame_edit,
        text='Fabricante',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=0, column=4, padx=10, pady=20, sticky='w')

    manufacturer = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=manufacturer)
    textbox.grid(row=0, column=5)

    label = ttk.Label(
        label_frame_edit,
        text='Voltagem de uso',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=1, column=0, padx=10, pady=20, sticky='w')

    voltage = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=voltage)
    textbox.grid(row=1, column=1)

    label = ttk.Label(
        label_frame_edit,
        text='Part Number',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=1, column=2, padx=10, pady=20, sticky='w')

    part_number = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=part_number)
    textbox.grid(row=1, column=3)

    label = ttk.Label(
        label_frame_edit,
        text='Tamanho',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=1, column=4, padx=10, pady=20, sticky='w')

    size = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=size)
    textbox.grid(row=1, column=5)

    label = ttk.Label(
        label_frame_edit,
        text='Unidade de medida',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=2, column=0, padx=10, pady=20, sticky='w')

    unit_measurement = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=unit_measurement)
    textbox.grid(row=2, column=1)

    label = ttk.Label(
        label_frame_edit,
        text='Tipo de ferramenta',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=2, column=2, padx=10, pady=20, sticky='w')

    _type = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=_type)
    textbox.grid(row=2, column=3)

    label = ttk.Label(
        label_frame_edit,
        text='Material da ferramenta',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=2, column=4, padx=10, pady=20, sticky='w')

    material = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=material)
    textbox.grid(row=2, column=5)

    label = ttk.Label(
        label_frame_edit,
        text='Tempo máximo de reserva',
        background=color_map['background_central'],
        foreground=color_map['text'],
    )
    label.grid(row=3, column=0, padx=10, pady=20, sticky='w')

    max_reservation_time = StringVar()
    textbox = ttk.Entry(label_frame_edit, textvariable=max_reservation_time)
    textbox.grid(row=3, column=1)

    button_add = ttk.Button(
        label_frame_edit,
        text='Adicionar',
        command=lambda: [
            services.create_tool(
                id=_id.get(),
                description=description.get(),
                manufacturer=manufacturer.get(),
                voltage=voltage.get(),
                part_number=part_number.get(),
                size=size.get(),
                unit_measurement=unit_measurement.get(),
                type=_type.get(),
                material=material.get(),
                max_reservation_time=max_reservation_time.get(),
            ),
            tools_page(frame_master),
        ],
    )
    button_add.grid(row=4, column=0, padx=10, pady=20)

    button_update = ttk.Button(
        label_frame_edit,
        text='Atualizar',
        command=lambda: [
            services.update_tool(
                id=_id.get(),
                description=description.get(),
                manufacturer=manufacturer.get(),
                voltage=voltage.get(),
                part_number=part_number.get(),
                size=size.get(),
                unit_measurement=unit_measurement.get(),
                type=_type.get(),
                material=material.get(),
                max_reservation_time=max_reservation_time.get(),
            ),
            tools_page(frame_master),
        ],
    )
    button_update.grid(row=4, column=1, padx=10, pady=20)

    button_delete = ttk.Button(
        label_frame_edit,
        text='Excluir',
        command=lambda: [services.delete_tool(id=_id.get()), tools_page(frame_master)],
    )
    button_delete.grid(row=4, column=2, padx=10, pady=20)

    button_clear = ttk.Button(
        label_frame_edit,
        text='Limpar Campos',
        command=lambda: tools_page(frame_master),
    )
    button_clear.grid(row=4, column=3, padx=10, pady=20)
