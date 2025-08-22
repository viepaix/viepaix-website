import reflex as rx

config = rx.Config(
    app_name="mysite",
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV3Plugin(),
    ],
)
