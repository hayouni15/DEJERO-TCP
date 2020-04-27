class TLV:
    def __init__(self, data_type, data_length, data_value):
        self.type = data_type
        self.length = data_length
        self.value = data_value
