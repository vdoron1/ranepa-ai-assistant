from vkbottle import Keyboard, KeyboardButtonColor, Text  # type: ignore

DidAnsweredKeyboard = (
    Keyboard(inline=True)
    .row()
    .add(Text("Да"), color=KeyboardButtonColor.PRIMARY)
    .add(Text("Нет"), color=KeyboardButtonColor.SECONDARY)
)
