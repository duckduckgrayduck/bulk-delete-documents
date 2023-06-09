from documentcloud.addon import AddOn, SoftTimeOutAddOn
class BulkDelete(SoftTimeOutAddOn):
    def main(self):
        confirm = self.data.get("confirm")
        if confirm is not None and confirm is True:
            for document in self.get_documents():
                document.delete()
        else: 
            self.set_message("You did not confirm, this Add-On did nothing.")

if __name__ == "__main__":
    BulkDelete().main()
