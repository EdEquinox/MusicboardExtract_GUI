# __init__.py

# Import any necessary modules or packages here

from .modules.app_setup import setup_app
from .modules.loading_screen_setup import setup_loading_screen
from .modules.button_setup import setup_buttons
from .modules.input_module import input_module_label, input_module_form
from .utils.process_loading import process_and_update
from .modules.input_module import configure_button
from .modules.extract_data import extract_list
from .modules.extract_data import extract_list_album
from .modules.extract_data import extract_list_later
from .modules.extract_data import extract_list_reviews
import os
import sys
import pkg_resources

# Define any global variables or constants here

APP_GEOMETRY = "800x600"

BACKGROUND_IMG = pkg_resources.resource_filename('musicboardextract_gui', 'assets/Sprinkle.png')
ICON_PATH = pkg_resources.resource_filename('musicboardextract_gui', 'assets/logo_musicboard.ico')

# Define any functions or classes here

# Optionally, include any initialization code here
