from utils.tlv import tlv
class Parser:
    def __init__(self,message):
        self.message=message

    def parse(self):
        socket_tlv=[]
        message=self.message
        while len(message,)>0:
            data_type,message=self.get_type(message)
            data_length,message=self.get_length(message)
            data_content,message=self.get_data(data_length,message)

            data_chank=tlv(data_type,data_length,data_content)
            socket_tlv.append(data_chank)

        return socket_tlv


    def get_type(self,message):
        data_type=message[0:4]
        message=message[4:]
        return data_type,message


    def get_length(self,message):
        data_length=message[0:8]
        message=message[8:]
        return int(data_length,16),message
        #return data_length,message


    def get_data(self,length,message):
        n=2
        data_string=message[0:2*length]
        message=message[2*length:]
        #message.replace(message[0:length], b'')
        return [data_string[i:i + n] for i in range(0, len(data_string), n)],message

    def print_parsed_data(self,TLV_blob,client_address):

        for tlv_blob in TLV_blob:
            if tlv_blob.type == b'E110':
                TYPE='[Hello]'
            elif tlv_blob.type==b'DA7A':
                TYPE='[Data]'
            else:
                TYPE='[Goodbye]'

            print( '[',client_address[0],':',client_address[1],']',TYPE,' [',tlv_blob.length,'] ', tlv_blob.value)

