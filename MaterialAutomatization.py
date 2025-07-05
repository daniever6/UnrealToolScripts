import unreal


classType = 'StaticMeshActor'# Variable que flexibiliza el tipo de ctor que se quiere seleccionar
selected_meshes = []# Lista que guarda los static meshes seleccionados
#funcion main que contenga todas las funciones


def main():
    
    #Elegir todos los static meshes que se quiere automatizar, en este caso todos los static meshes seleccionados con raton
    getSelectedActor()
    getSelectionContectBrowser()# coger el material seleccionado en el content browser
    return
    
def getSelectedActor():# Escoger todos los actores seleccionados en el level
    EAS = unreal.EditorActorSubsystem()# Instanciar EAS para usar sus funciones
    
    selected_actors = EAS.get_selected_level_actors()# Mediante selected_level_actors, se escogen todos los actores
    for actor in selected_actors:
        if (actor.get_class().get_name() == classType):# compruebo si el actor es static mesh
           selected_meshes.append(actor)# Los añado a la lista de static meshes seleccionados
    #return selected_meshes# Y devuelvo la lista, no es seguro si es necesario, ya que es una variable global



def getMaterialData(material_data):
    #EAL = unreal.EditorAssetLibrary()# Get the Editor Asset Library instance
    #aterial_data = EAL.load_asset('/Game/TFM/Material_Enviroment/MI_MasterSnowMask')# Find the asset data for the specified material
    #Quiza no es necesario ya que se ha escogido el material en la previa funcion getSelectionContectBrowser
    #if(material_data.get_class().get_name() == 'MaterialInstanceConstant' or material_data.get_class().get_name() == 'Material'):
        #setMaterialData(material_data)# Set the material data for the selected static meshes
    return

def setMaterialData(material_data):
    for actor in selected_meshes: #por actor seleccionado
        static_mesh_component = actor.static_mesh_component #se accede al componente de static mesh del actor
        print(("Voy a poner materiales a " + actor.get_name()))#Comprobacion para ver si se aplica correctamente al actor
        static_mesh_component.set_material(0, material_data)# Se le asigna el material al static mesh
        if static_mesh_component.get_material(0) == material_data:#para controlarlo mejor se usa un if.
            print("Material set successfully")
        else:
            print("Failed to set material")
    selected_meshes.clear()# Quito todos los static meshes y refresco la lista para la siguiente operacion

def setMaterial(selectedActors,actorIndex,materialIndex,material_data):
    print(("Voy a poner materiales"+ material_data.get_name() + "a " + selectedActors[actorIndex].get_name()))#Comprobacion para ver si se aplica correctamente al actor
    selectedActors[actorIndex].static_mesh_component.set_material(materialIndex,material_data)# Se le asigna el material al static mesh

        

def getSelectionContectBrowser():#Coger el material seleccionado en el content browser
    EUL = unreal.EditorUtilityLibrary()# Instanciar la clase EditorUtilityLibrary para usar sus funciones

    selectedAssets = EUL.get_selected_assets()# coger todos los assets que estan seleccionados en el content browser
    for asset in selectedAssets:
        #Se escoge el primer material que se encuentre, si no es un material, se salta
        if(asset.get_class().get_name() == 'MaterialInstanceConstant' or asset.get_class().get_name() == 'Material'):
            setMaterialData(asset)#llamar la siguiente funcion 

def getSelectedMeshes(ListView,classType="StaticMeshActor"):# Escoger todos los actores seleccionados en el level
    import unreal
    EAS = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)# Instanciar EAS para usar sus funciones
    ListView = unreal.EditorUtilityListView()
    meshes = []
    ListView.clear_list_items()#vacio la lista 
    selectedActors = EAS.get_selected_level_actors()# Mediante selected_level_actors, se escogen todos los actores
    for actor in selectedActors:
        if(actor.get_class().get_name() == classType):# compruebo si el actor es static mesh
            meshes.append(actor)# Los añado a la lista de static meshes seleccionados
    return meshes# Devuelvo la lista de actores seleccionados

def getPreviousMaterial(selectedActors,actorIndex,materialIndex,material_data):
    return selectedActors[actorIndex].static_mesh_component.get_material(materialIndex)# Devuelvo el material que tiene el actor en ese momento

def setMaterialUV(selectedActors,actorIndex,UV,materialindex):
    import unreal
    static_mesh = selectedActors[actorIndex].static_mesh_component
    uv = unreal.LinearColor(UV,UV,0,0)
    material_util = unreal.MaterialEditingLibrary()
    material_util.set_material_instance_vector_parameter_value(static_mesh.get_material(materialindex), "UVs / Offset", uv)

def saveInstanceCopy(asset, path):
    import unreal
    EAL = unreal.EditorAssetLibrary()
    tools = unreal.AssetToolsHelpers.get_asset_tools()
    tools.create_asset(asset.name,asset.asset_class_path)

def getMaterialType():
    import unreal
    EUL = unreal.EditorUtilityLibrary()# Instanciar la clase EditorUtilityLibrary para usar sus funciones
    selectedAssets = EUL.get_selected_assets()# coger todos los assets que estan seleccionados en el content browser
    EAS = unreal.EditorActorSubsystem()# Instanciar EAS para usar sus funciones
    selected_actors = EAS.get_selected_level_actors()# Mediante selected_level_actors, se escogen todos los actores
    it = unreal.ObjectIterator()
    for asset in selected_actors:
        for material in asset.static_mesh_component.get_materials():
            if material == unreal.Material():
                continue
            else:
                materialParent  = material.parent
            asset_path = unreal.SystemLibrary.get_path_name(materialParent)# Get the path of the selected asset
            print(asset_path)
            for x in it:
                if isinstance(x, unreal.MaterialExpression) and x.get_path_name().startswith(asset_path):
                    if(x.get_class().get_name() == "MaterialExpressionMaterialAttributeLayers"):
                        print(material.get_name() + " de " + asset.get_name() + " Es un material de tipo layers")
    