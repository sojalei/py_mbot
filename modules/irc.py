from bases import BaseTelegramModule


class TelegramModule(BaseTelegramModule):
    def __init__(self, telegram_api):
        super(TelegramModule, self).__init__(telegram_api)
        self._telegram_api.register_command(['me'], self.me)

    def help(self, message, args):
        self._telegram_api.send_text_message(message.chat_id, 'Equivalent of IRC /me command')

    def me(self, message, args):
        self._telegram_api.send_text_message(message.chat_id,
                                             f"{message.from_user.name} {' '.join(args)}")