class Message:
    def __init__(self, content, read_status=False):
        self.content = content
        self.read_status = read_status

original_message = Message("Hey there!")


read_message = original_message
read_message.read_status = True

if original_message is not read_message:
    print("The message has been read.")
else:
    print("The message hasn't been read yet.")
