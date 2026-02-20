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
from .common import *

class SEDAIA_PT_skin_panel(CorePanel):
    """
    Panel for Minecraft Skin Utility operations.
    """
    bl_label = "Skin Utility"
    bl_idname = "SEDAIA_PT_skin_panel"
    bl_order = 0

    def draw(self, context):
        ui = self.layout
        ui.label(text="Skin Utility Panel")

classes = [
    SEDAIA_PT_skin_panel,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
