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

import bpy
from bpy.types import AddonPreferences
from bpy.props import BoolProperty

class SEDAIA_AddonPreferences(AddonPreferences):
    """
    Main preferences for the Sedaia Rig Interfaces addon.
    """
    bl_idname = __package__

    show_debug_info: BoolProperty(
        name="Show Debug Information",
        description="Enable additional logging and debug tools in the UI",
        default=False
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "show_debug_info")

def get_preferences(context=None):
    """
    Utility function to get the addon preferences.
    """
    if not context:
        context = bpy.context
    return context.preferences.addons[__package__].preferences

classes = [
    SEDAIA_AddonPreferences,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
