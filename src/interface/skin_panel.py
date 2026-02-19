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

class SEDAIA_PT_skin_utility(T.Panel):
    """
    Main panel for the Sedaia Skin Utility.
    """
    bl_label = "Sedaia Skin Utility"
    bl_idname = "SEDAIA_PT_skin_utility"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Sedaia"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Skin Downloader coming soon...")

classes = [
    SEDAIA_PT_skin_utility,
]

def register():
    for cls in classes:
        U.register_class(cls)

def unregister():
    for cls in reversed(classes):
        U.unregister_class(cls)

import bpy
import bpy.types as T
from ..utils import config as C

class SEDAIA_PT_skin_panel(T.Panel):
    """
    Panel for Minecraft Skin Utility operations.
    """
    bl_label = "Skin Utility"
    bl_idname = "SEDAIA_PT_skin_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Sedaia Skin Utility"
    bl_order = 0

    @classmethod
    def poll(cls, context):
        try:
            r = context.active_object
            utility_bone_name = C.get_setting("utility_bone_name", "Sedaia.Skin_Utility_Config")
            if r and r.type == "ARMATURE" and r.data:
                if context.active_object.pose.bones.get(utility_bone_name) is not None:
                    return True
            return False
        except (AttributeError, KeyError, TypeError):
            return False

    def draw(self, context):
        layout = self.layout
        rig = context.active_object
        rig_bones = rig.pose.bones
        
        utility_bone_name = C.get_setting("utility_bone_name", "Sedaia.Skin_Utility_Config")
        skin_path = C.get_setting("skin_path", "") # Fallback will be handled in ops if needed

        try:
            skinProp = rig_bones.get(utility_bone_name)
        except (KeyError):
            skinProp = None
            
        if skinProp is not None:
            # Username Section
            p_row = layout.row()
            p_row.label(text="Minecraft Username")

            b_col = layout.column(align=True)
            c_row = b_col.row()
            c_row.prop(skinProp, '["Username"]', text="")
            
            c_row = b_col.row(align=True)
            # Operators might not exist yet, we'll use placeholder IDs if they are not yet implemented in src
            c_row.operator("sedaia.skin_router", icon="URL", text="Change Skin")
            op = c_row.operator("wm.path_open", icon="FILEBROWSER", text="Player Data")
            op.filepath = skin_path if skin_path else ""

            layout.separator(type="LINE")

            # Options Section
            layout.label(text="Options")
            
            b_col = layout.column()
            b_col.prop(skinProp, '["SyncArms"]', toggle=False, text="Sync Arm Type")
            b_col.prop(skinProp, '["SyncCape"]', toggle=False, text="Sync Cape Status")
            b_col.prop(skinProp, '["SyncName"]', toggle=False, text="Set Rig Name to Username")

classes = [
    SEDAIA_PT_skin_panel,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
