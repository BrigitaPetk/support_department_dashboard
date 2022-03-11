import win32com.client
import os
import re


class AttachmentRetriever():
    def retrieve(self, download_direktorija):

        outlook = win32com.client.Dispatch('outlook.application').GetNamespace("MAPI")

        # folder_dashboard = outlook.Folders("DE Festo MBX TRS RawData Global")
        # inbox_dashboard = folder_dashboard.Folders("Posteingang")

        # folder_personal =outlook.Folders("LT Festo MBX TSS Complaints")
        # inbox_personal = folder_personal.Folders("Inbox")

        # inboxs = [inbox_dashboard, inbox_personal]
        inbox =outlook.GetDefaultFolder(6)

        # for inbox in inboxs:
        messages = inbox.Items


        if len(messages) == 0:
            print("There aren't any messages in this folder")
            exit()


        for message in list(messages)[-10:]:     
            subject = message.Subject
            sender = message.SenderEmailAddress
            time =  message.Senton.date()
            attachment = message.Attachments
            print (subject, sender, time, attachment)

            if len(attachment) == 0:
                print("No attachments")
            else:
                for attac in attachment:
                    name = "PROD_Cronjob_Tickets_all_queues_last_7_days" 
                    if re.search(name, str(attac)):
                        attac.SaveASFile(os.path.join(download_direktorija, str(attac))) 
                        print(f"Saved {str(attac)} attachments")
                    else:
                        print(f"wrong attachment {str(attac)}")
                

            




