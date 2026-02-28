from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_1", "click")
  def button_1_click(self, **event_args):

    self.button_1.text = "Support Form Sent"
    self.button_1.icon = "fa:check"
    if self.button_1.text == "":
      self.button_1.text = "Fill out all fields first."

    
    """This method is called when the button is clicked"""
    pass
