


class SessionHelper:

    def __init__(self, app):
        self.app = app




    def login(self, username, password):
        # login
        wd = self.app.wd
        wd.get("http://localhost/addressbook/delete.php?part=12;13;")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


    def logout(self):
        # logout
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()