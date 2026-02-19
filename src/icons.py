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
import bpy.utils.previews

# Global variable to hold the icon collection
preview_collections = {}


def register():
    """
    Registers the custom icons.
    """
    pcoll = bpy.utils.previews.new()

    # Path to the icons directory
    icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    # Load all .png files in the icons directory
    if os.path.exists(icons_dir):
        for filename in os.listdir(icons_dir):
            if filename.endswith(".png"):
                name = os.path.splitext(filename)[0]
                filepath = os.path.join(icons_dir, filename)
                pcoll.load(name, filepath, 'IMAGE')

    preview_collections["main"] = pcoll


def unregister():
    """
    Unregisters the custom icons.
    """
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()


def get_icon(name):
    """
    Returns the custom icon with the given name.

    Args:
        name (str): The name of the icon (without extension).

    Returns:
        int: The icon ID if found, otherwise 0.
    """
    pcoll = preview_collections.get("main")
    if pcoll and name in pcoll:
        return pcoll[name].icon_id
    return 0
