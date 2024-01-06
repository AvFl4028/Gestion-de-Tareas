from reactpy import component, html


@component
def btn(text):
    return html.a({"href": "/"}, text)


@component
def NavBar():
    return html.nav(
        {"class_name": "navbar navbar-expand-lg navbar-dark bg-dark"},
        html.div(
            {"class_name": "container-fluid"},
            html.a({"class_name": "navbar-brand text-center"}, "Gestion de tareas"),
        ),
    )


@component
def List(value):
    return html.li({}, value)


@component
def Card(title, description, time):
    return html.div(
        {"class_name": "card text-center"},
        html.div({"class_name": "card-header"}, "Tarea"),
        html.div(
            {"class_name": "card-body"},
            html.h5({"class_name": "card-title"}, title),
            html.p({"class_name": "card-text"}, description),
        ),
        html.div({"class_name": "card-footer text-muted"}, f"Hora: {time}")
    )
