import reflex as rx

config = rx.Config(
    app_name="mysite",
    plugins=[rx.plugins.TailwindV3Plugin()],
    head=["<meta name='impact-site-verification' value='19317128-c13a-4f19-af50-28acf6cab79d'>"],
    show_built_with_reflex=False,
)
