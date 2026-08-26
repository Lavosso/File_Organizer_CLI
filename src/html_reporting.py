import markdown


def rewrite_data_in_markdown(data: dict[str, list], title: str) -> str:
    md_text = f"# General Report: {title}\n"
    for key, value in data.items():
        md_text += f"## {key}:\n"
        for item in value:
            md_text += f"- {item}\n"
    return md_text


def rewrite_markdown_into_html(markdown_data: str) -> str:
    html_body = markdown.markdown(markdown_data)
    html_full = f"""<!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>Dokument HTML</title>
    </head>
    <body>
        {html_body}
    </body>
    </html>"""
    return html_full
