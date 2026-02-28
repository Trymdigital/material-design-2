from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def submit(self, **event_args):
    name = self.name_box.text
    Notification("Name Recorded").show()

    email = self.email_box.text
    Notification("Email Recorded").show()

    desc = self.desc_box.text
    Notification("Desc Recorded").show()

    anvil.server.call('add_feedback', name, email, desc)
    Notification("Feedback submitted!").show()

    self.clear_inputs()

  def clear_inputs(self):
    self.name_box.text = ""
    self.email_box.text = ""
    self.desc_box.text = ""

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    if self.name_box.text == "" or self.email_box.text == "" or self.desc_box.text == "":
      self.button_1.text = "Fill out all fields first."
      self.button_1.icon = "fa:warning"
    else:
      self.submit()
      self.button_1.text = "Support Form Sent"
      self.button_1.icon = "fa:check"

  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):
    self.submit()

  @handle("link_1", "click")
  
  def link_1_click(self, **event_args):
    
    """This method is called when the link is clicked"""
    pass
