
def find_mesh_by_texture_name(texture_name):
    import unreal
    asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
    
    static_mesh_class = unreal.TopLevelAssetPath("/Script/Engine", "StaticMesh")

    mesh_assets = asset_registry.get_assets_by_class(static_mesh_class, True)
    
    
    matching_meshes = []
    for asset in mesh_assets:
        if asset.asset_name == texture_name:
            print(f"Found matching mesh: {asset.get_asset().get_name()}")
            matching_meshes.append(asset.get_asset())
    
    return matching_meshes[0] if matching_meshes else None


def set_button_image(texture):
    import unreal
    if not texture:
        unreal.log_error(f": {texture} is not a valid texture.")
        return

    new_style = unreal.ButtonStyle()    
    
    brush = unreal.SlateBrush()
    brush.resource_object = texture
    brush.draw_as = unreal.SlateBrushDrawType.IMAGE 
    brush.tint_color = unreal.SlateColor(unreal.LinearColor(1, 1, 1, 1))

    brush_hovered = unreal.SlateBrush()
    brush_hovered.resource_object = texture
    brush_hovered.draw_as = unreal.SlateBrushDrawType.IMAGE 
    brush_hovered.tint_color = unreal.SlateColor(unreal.LinearColor(0.1,0.1,0.1,1))

    brush_pressed = unreal.SlateBrush()
    brush_pressed.resource_object = texture
    brush_pressed.draw_as = unreal.SlateBrushDrawType.IMAGE 
    brush_pressed.tint_color = unreal.SlateColor(unreal.LinearColor(0.03,0.03,0.03,1))

    new_style.normal = brush
    new_style.hovered = brush_hovered
    new_style.pressed = brush_pressed


    return new_style

def get_selected_actors():
    import unreal
    
    editor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    selected_actors = editor_subsystem.get_selected_level_actors()

    target_actor = None

    if len(selected_actors) > 1:
        for actor in selected_actors:
            if actor != selected_actors[0]:  # 跳过父物体
                if isinstance(actor, unreal.StaticMeshActor):
                    target_actor = actor
                    return target_actor
    