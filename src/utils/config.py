# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import bpy.utils as U
from . import file as F

def get_default_config_path():
    """
    Returns the default path for the configuration file.
    """
    # Use extension_path_user if available, otherwise fallback to local folder
    # Extension path is standard for Blender extensions
    try:
        base_path = U.extension_path_user(__package__, create=True)
    except:
        base_path = os.path.dirname(os.path.dirname(__file__))

    return os.path.join(base_path, "config.json")

def get_config_data():
    """
    Loads configuration data from the custom path specified in preferences.
    """
    from ..prefs import get_preferences
    prefs = get_preferences()
    path = prefs.config_path
    
    if not path:
        path = get_default_config_path()
        # Don't update prefs here as it might cause recursion or be inappropriate 
        # during registration, but provide it as fallback.

    return F.read_json(path)

def save_config_data(data):
    """
    Saves configuration data to the custom path specified in preferences.
    """
    from ..prefs import get_preferences
    prefs = get_preferences()
    path = prefs.config_path
    
    if not path:
        path = get_default_config_path()
        prefs.config_path = path

    return F.write_json(path, data)

def get_setting(key, default=None):
    """
    Gets a setting from the custom config.
    """
    config = get_config_data()
    return config.get(key, default)

def set_setting(key, value):
    """
    Sets a setting in the custom config.
    """
    config = get_config_data()
    config[key] = value
    return save_config_data(config)
