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
import bpy.types as T
import bpy.utils as U
import bpy.props as P
import bpy.ops as O

class SEDAIA_OT_open_config_path(T.Operator):
    """
    Opens the current configuration folder in the OS file explorer.
    """
    bl_idname = "sedaia.open_config_path"
    bl_label = "Open Config Folder"

    def execute(self, context):
        from .utils import file as F
        path = get_preferences(context).config_path
        
        import os
        dir_path = os.path.dirname(path) if path else None
        
        if F.open_path(dir_path):
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, f"Could not open path: {dir_path or 'Default'}")
            return {'CANCELLED'}

class SEDAIA_AddonPreferences(T.AddonPreferences):
    """
    Main preferences for the Sedaia Rig Interfaces addon.
    """
    bl_idname = __package__

    show_debug_info: P.BoolProperty(
        name="Show Debug Information",
        description="Enable additional logging and debug tools in the UI",
        default=False
    )

    config_path: P.StringProperty(
        name="Config Path",
        description="Path to the Sedaia Rig Interfaces config file",
        default="",
        subtype="FILE_PATH"
    )


    def draw(self, context):
        layout = self.layout
        
        # Initialize default config path if empty
        if not self.config_path:
            from .utils import config
            self.config_path = config.get_default_config_path()

        layout.prop(self, "show_debug_info")
        
        box = layout.box()
        box.label(text="External Configuration")
        box.prop(self, "config_path")
        box.operator("sedaia.open_config_path", icon='FILE_FOLDER')

def get_preferences(context=None):
    """
    Utility function to get the addon preferences.
    """
    if not context:
        context = bpy.context
    return context.preferences.addons[__package__].preferences

classes = [
    SEDAIA_OT_open_config_path,
    SEDAIA_AddonPreferences,
]

def register():
    for cls in classes:
        U.register_class(cls)

def unregister():
    for cls in reversed(classes):
        U.unregister_class(cls)
