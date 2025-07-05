import unreal

def Entry():
    print("Asegurate que el metodo no este decrapetado para tener el codigo actualizado")


def listAssetPaths():
    EAL = unreal.EditorAssetLibrary()

    assetPaths = EAL.list_assets('/Game/TFM/Model')# List all assets in the specified path

    for assetpath in assetPaths:
        print(assetpath)

def getSelectionContectBrowser():#Get selected assets in the content browser
    EUL = unreal.EditorUtilityLibrary()# Get the Editor Utility Library instance

    selectedAssets = EUL.get_selected_assets()# Get selected assets in the content browser
    for asset in selectedAssets:
        print(asset)

def getAllActor():
    EAS = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)# Get the Editor Asset Subsystem instance
    #EAS = unreal.EditorActorSubsystem()# Get the Editor Actor Subsystem instance
    actors = EAS.get_all_level_actors()# Get all actors in the level

    selected_actors = EAS.get_selected_level_actors()# Get selected actors in the level
    for actor in actors:
        print(actor)# Print the name of each actor

    for actor in selected_actors:
        print(actor.get_name())# Print the name of each selected actor

def getSelectedActor():
    EAS = unreal.EditorActorSubsystem()# Get the Editor Actor Subsystem instance

    selected_actors = EAS.get_selected_level_actors()# Get selected actors in the level
    for actor in selected_actors:
        
        print(actor)# Print the name of each selected actor

def getWorldProperty():
    #world = unreal.EditorLevelLibrary
    return

def getAssetClass(classType):
    EAL = unreal.EditorAssetLibrary()# Get the Editor Asset Library instance

    assetpath = EAL.list_assets('/Game/TFM/Model')
    
    assets = []# List to store assets of the specified class type
    for asset in assetpath:
        assetData = EAL.find_asset_data(asset)
        assetClass = assetData.asset_class_path.asset_name# Get the class of the asset
        if assetClass == classType:
            assets.append(assetData.get_asset())# Add the asset to the list if it matches the class type
    #for asset in assets:
        #print(asset.get_name())
    return assets# Return the list of assets of the specified class type

def getStaticMeshData():
    staticMeshs = getAssetClass('StaticMesh')# Get all static meshes in the specified path
    for staticMesh in staticMeshs:
        #assetImportData = staticMesh.get_editor_property('asset_import_data')# Get the asset import data of the static mesh
        #fbxFilePath = assetImportData.extract_filenames()   # Extract the FBX file path from the asset import data
        #print(fbxFilePath)
        
        lodGroup = staticMesh.get_editor_property('lod_group')
        print(lodGroup)# Print the LOD group of the static mesh

        if lodGroup == 'None':
            if staticMesh.get_num_lods() ==1 :
            
                #staticMesh.set_editor_property('lod_group',)