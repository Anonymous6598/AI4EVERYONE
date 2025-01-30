import flet, g4f, g4f.Provider

def main(page: flet.Page) -> None:

    def ai_response(e: str) -> None:
        user_query: list[dict[str, str]] = [{f"role": f"user", f"content": f"{input_textfield.value}"}]
        response: str = g4f.ChatCompletion.create(model=f"gpt-4o-mini", provider=g4f.Provider.DDG, messages=user_query)

        chat_field.value += f"""
USER:\n{input_textfield.value}\nChatBot:\n{response}\n
"""

        input_textfield.value = f""   

        page.update()

    page.title = f"AI4EVERYONE"

    chat: str = f"""
Welcome to early access of AI4EVERYONE - free AI chatbot for everyone.
"""

    chat_field: flet.Markdown = flet.Markdown(chat, selectable=True, extension_set=flet.MarkdownExtensionSet.GITHUB_WEB, soft_line_break=True, code_theme="atom-one-dark")

    input_textfield: flet.TextField = flet.TextField(on_submit=ai_response)

    page.add(flet.Column([chat_field], height=600, scroll=f"auto"), flet.Column([input_textfield], alignment=flet.MainAxisAlignment.END, horizontal_alignment=flet.CrossAxisAlignment.END, expand=True))

    page.update()

if __name__ == f"__main__":
    flet.app(main, view=flet.WEB_BROWSER)