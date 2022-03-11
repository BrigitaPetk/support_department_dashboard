from exchangelib import Credentials, Account, FileAttachment, ItemAttachment, Message
import os.path
import os

class AttachmentRetrieverServer():
    def retrieve_server(self, download_direktorija):
        credentials = Credentials(os.environ["pasto_adresas"], os.environ["pasto_paswordas"])
        account = Account(os.environ["pasto_adresas"], credentials=credentials, autodiscover=True)

        a = account
        for item in a.inbox.filter(subject__contains='PROD_Cronjob_Tickets_all_queues_last_7_days'):   #[:5]
            for attachment in item.attachments:
                if isinstance(attachment, FileAttachment):
                    local_path = os.path.join(download_direktorija, attachment.name)
                    with open(local_path, 'wb') as f:
                        f.write(attachment.content)
                    print(f'Laiskas {item.subject} Rastas attachmentas ------------------{str(attachment.name)} ')
                elif isinstance(attachment, ItemAttachment):
                    if isinstance(attachment.item, Message):
                        print(attachment.item.subject, attachment.item.body)