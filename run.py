from SourceQueryBot import SourceQueryBot
from SourceQueryBot.settings import Category, Server


bot_client = SourceQueryBot(
    [
        Category(
            "Minimalistic Drp",
            705852327550124062,
            0xffffff,
            [
                Server("163.172.51.55"),
            ]
        ),
    ],
    smart_presence=True
)

if __name__ == "__main__":
    bot_client.run("ODQ2ODMzNTg1MTA1MjcyODcy.YK1RPA._Th26TyDjh7whb_ultbKRM0c3lo")
