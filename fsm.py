from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "計算理論期末考"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "營期"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "寒假"
    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "電子學期末考"

    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "控制工程期末考"

    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "電儀表學期末考"
    def is_going_to_list(self, event):
        text = event.message.text
        return text.lower() == "list"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "2022/01/12")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "2022/01/15-2022/01/28")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "2022/01/14")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")

    def on_enter_list(self, event):
        print("I'm entering list")

        reply_token = event.reply_token
        send_text_message(reply_token, "計算理論期末考/營期/寒假/電子學期末考/控制工程期末考/電儀表學期末考")
        self.go_back()

    def on_exit_list(self):
        print("Leaving list")

    def on_enter_state4(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        send_text_message(reply_token, "2022/01/11")
        self.go_back()

    def on_exit_state4(self):
        print("Leaving state4")
    def on_enter_state5(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "2022/01/13")
        self.go_back()

    def on_exit_state5(self):
        print("Leaving state5")
    def on_enter_state6(self, event):
        print("I'm entering state6")

        reply_token = event.reply_token
        send_text_message(reply_token, "2022/01/07")
        self.go_back()

    def on_exit_state6(self):
        print("Leaving state6")