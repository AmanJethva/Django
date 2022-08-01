# from channels.consumer import SyncConsumer, AsyncConsumer
# from channels.exceptions import StopConsumer

# class MySyncConsumer (SyncConsumer):
#     def websocket_connect(self,event):
#         print('Websocket connected...',event)
#         self.send({
#             'type':'websocket accept',
#         })

#     def websocket_recieve(self,event):
#         print('Message received from client',event)
#         print(event['text'])
#         self.send({
#             'type':'websocket.send',
#             'text':'Message sent to client'
#             })

#     def websocket_disconnected(self,event):
#         print('websocket disconnected...',event)
#         raise StopConsumer()
