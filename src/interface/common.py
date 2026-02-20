import bpy.types as T

class CorePanel(T.Panel):
    """
    Base class for all Sedaia panels.
    """
    bl_category = "Sedaia"
    bl_label = "Sedaia Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw_header(self, context):
        layout = self.layout
        layout.label(text=self.bl_label, icon="PROPERTIES")