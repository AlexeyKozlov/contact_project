
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fillout(self, kon):
        # create contact
        wd = self.app.wd
        self.open_contacts_page()
        self.fill_contact_form(kon)



    def type_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, kon):
        wd = self.app.wd
        self.type_contact("firstname", kon.first_name)
        self.type_contact("lastname", kon.last_name)
        self.type_contact("nickname", kon.nick)
        self.type_contact("title", kon.title)
        self.type_contact("company", kon.organization)
        self.type_contact("address", kon.address)
        self.type_contact("mobile", kon.cell)
        self.type_contact("email", kon.email)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[32]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[32]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").click()
        self.type_contact("byear", kon.birth)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()



    def open_home_page(self):
        wd = self.app.wd
        return wd.find_element_by_link_text("home").click

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()



    def modify_first_contact(self, new_contact_name):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # open modofication form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #fill the form
        self.fill_contact_form(new_contact_name)
        # submit
        wd.find_element_by_name("update").click()
