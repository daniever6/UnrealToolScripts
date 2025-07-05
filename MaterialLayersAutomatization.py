def vertexColor():
    import unreal# Se importa la libreria unreal
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()# Se obtiene la herramienta de asset
    index = 0
    it = unreal.ObjectIterator()
    list = unreal.EditorAssetLibrary.list_assets("/Game/TechArt/Materials/LayeringSystem/Masters",recursive=False,include_folder=False)
    print(list)
    for asset in list:# Se listan todos los assets que hay en la carpeta
        CompleteName = asset.partition(".")
        assetName = CompleteName[2].partition("_")
        assetSubfix = assetName[2].partition("_")
        print(assetSubfix)
        try:
            if(assetSubfix[0]=="VertexColor" and assetSubfix[-1].isnumeric()):
                index = int(assetSubfix[-1])+1 
        except:
                index = 0
    asset_tools.create_asset("MIMLS_VertexColor_"+str(index),"/Game/TechArt/Materials/LayeringSystem/Masters",unreal.MaterialInstanceConstant,unreal.MaterialInstanceConstantFactoryNew())# Se crea el asset
    material = unreal.EditorAssetLibrary.load_asset("/Game/TechArt/Materials/LayeringSystem/Masters/MIMLS_VertexColor_"+str(index))# Se carga el asset
    material.set_editor_property("parent",unreal.EditorAssetLibrary.load_asset("/Game/TechArt/Materials/LayeringSystem/MMLS_Base"))
    return "/Game/TechArt/Materials/LayeringSystem/Masters/MIMLS_VertexColor_"+str(index)


def znormal():
    import unreal# Se importa la libreria unreal
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()# Se obtiene la herramienta de asset
    index = 0
    it = unreal.ObjectIterator()
    list = unreal.EditorAssetLibrary.list_assets("/Game/TechArt/Materials/LayeringSystem/Masters",recursive=False,include_folder=False)
    print(list)
    for asset in list:# Se listan todos los assets que hay en la carpeta
        CompleteName = asset.partition(".")
        assetName = CompleteName[2].partition("_")
        assetSubfix = assetName[2].partition("_")
        print(assetSubfix)
        try:
            if(assetSubfix[0]=="ZNormal" and assetSubfix[-1].isnumeric()):
                index = int(assetSubfix[-1])+1 
        except:
                index = 0
    asset_tools.create_asset("MIMLS_ZNormal_"+str(index),"/Game/TechArt/Materials/LayeringSystem/Masters",unreal.MaterialInstanceConstant,unreal.MaterialInstanceConstantFactoryNew())# Se crea el asset
    material = unreal.EditorAssetLibrary.load_asset("/Game/TechArt/Materials/LayeringSystem/Masters/MIMLS_ZNormal_"+str(index))# Se carga el asset
    material.set_editor_property("parent",unreal.EditorAssetLibrary.load_asset("/Game/TechArt/Materials/LayeringSystem/MMLS_Base"))
    return "/Game/TechArt/Materials/LayeringSystem/Masters/MIMLS_ZNormal_"+str(index)

def triplanar():
    import unreal# Se importa la libreria unreal
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()# Se obtiene la herramienta de asset
    index = 0
    it = unreal.ObjectIterator()
    list = unreal.EditorAssetLibrary.list_assets("/Game/TechArt/Materials/LayeringSystem/Masters",recursive=False,include_folder=False)
    print(list)
    for asset in list:# Se listan todos los assets que hay en la carpeta
        CompleteName = asset.partition(".")
        assetName = CompleteName[2].partition("_")
        assetSubfix = assetName[2].partition("_")
        print(assetSubfix)
        try:
            if(assetSubfix[0]=="Triplanar" and assetSubfix[-1].isnumeric()):
                index = int(assetSubfix[-1])+1 
        except:
                index = 0
    asset_tools.create_asset("MIMLS_Triplanar_"+str(index),"/Game/TechArt/Materials/LayeringSystem/Masters",unreal.MaterialInstanceConstant,unreal.MaterialInstanceConstantFactoryNew())# Se crea el asset
    material = unreal.EditorAssetLibrary.load_asset("/Game/TechArt/Materials/LayeringSystem/MastersMIMLS_Triplanar_"+str(index))# Se carga el asset
    material.set_editor_property("parent",unreal.EditorAssetLibrary.load_asset("/Game/TechArt/Materials/LayeringSystem/MMLS_Base"))
    return "/Game/TechArt/Materials/LayeringSystem/MastersMIMLS_Triplanar_"+str(index)

def PuddleWorldTextureMask():
    import unreal# Se importa la libreria unreal
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()# Se obtiene la herramienta de asset
    index = 0
    it = unreal.ObjectIterator()
    list = unreal.EditorAssetLibrary.list_assets("/Game/TechArt/Materials/LayeringSystem/Masters",recursive=False,include_folder=False)
    print(list)
    for asset in list:# Se listan todos los assets que hay en la carpeta
        CompleteName = asset.partition(".")
        assetName = CompleteName[2].partition("_")
        assetSubfix = assetName[2].partition("_")
        print(assetSubfix)
        try:
            if(assetSubfix[0]=="PuddleWorldTextureMask" and assetSubfix[-1].isnumeric()):
                index = int(assetSubfix[-1])+1 
        except:
                index = 0
    asset_tools.create_asset("MIMLS_PuddleWorldTextureMask_"+str(index),"/Game/TechArt/Materials/LayeringSystem/Masters",unreal.MaterialInstanceConstant,unreal.MaterialInstanceConstantFactoryNew())# Se crea el asset
    material = unreal.EditorAssetLibrary.load_asset("/Game/TechArt/Materials/LayeringSystem/Masters/MIMLS_PuddleWorldTextureMask_"+str(index))# Se carga el asset
    material.set_editor_property("parent",unreal.EditorAssetLibrary.load_asset("/Game/TechArt/Materials/LayeringSystem/MMLS_Base"))
    return "/Game/TechArt/Materials/LayeringSystem/Masters/MIMLS_PuddleWorldTextureMask_"+str(index)

def RVT():
    import unreal# Se importa la libreria unreal
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()# Se obtiene la herramienta de asset
    index = 0
    it = unreal.ObjectIterator()
    list = unreal.EditorAssetLibrary.list_assets("/Game/TechArt/Materials/LayeringSystem/Masters",recursive=False,include_folder=False)
    print(list)
    for asset in list:# Se listan todos los assets que hay en la carpeta
        CompleteName = asset.partition(".")
        assetName = CompleteName[2].partition("_")
        assetSubfix = assetName[2].partition("_")
        print(assetSubfix)
        try:
            if(assetSubfix[0]=="RVT" and assetSubfix[-1].isnumeric()):
                index = int(assetSubfix[-1])+1 
        except:
                index = 0
    asset_tools.create_asset("MIMLS_RVT_"+str(index),"/Game/TechArt/Materials/LayeringSystem/Masters",unreal.MaterialInstanceConstant,unreal.MaterialInstanceConstantFactoryNew())# Se crea el asset
    material = unreal.EditorAssetLibrary.load_asset("/Game/TechArt/Materials/LayeringSystem/Masters/MIMLS_RVT_"+str(index))# Se carga el asset
    material.set_editor_property("parent",unreal.EditorAssetLibrary.load_asset("/Game/TechArt/Materials/LayeringSystem/MMLS_Base"))
    return "/Game/TechArt/Materials/LayeringSystem/Masters/MIMLS_RVT_"+str(index)
           
def setMaterialData(material_data,path):
    import unreal
    material = unreal.EditorAssetLibrary.load_asset(path)
    material
    
def duplicate_asset(asset):
    import unreal
    EAL = unreal.EditorAssetLibrary()


    original_path = EAL.get_path_name_for_loaded_asset(asset)
    print(EAL.get_path_name_for_loaded_asset(asset))
    if not original_path:
        print(f"Asset {asset} is not loaded or does not exist.")
        return None
    folder_path, asset_name = original_path.rsplit("/", 1)

    new_name = generate_unique_eal_name(asset_name,folder_path)
    print("The new name of the duplicated object is " + new_name)
    new_path = f"{folder_path}/{new_name}"
    print("The new path of the duplicated object is " + new_name)

    material = EAL.duplicate_loaded_asset(asset, new_path)

    if material:
         EAL.save_loaded_asset(material, True)
         print(f"Duplicated asset: {new_path}")
    else:
         print(f"Failed to duplicate asset: {original_path}, You are using the same asset that were duplicated")

    return material

def generate_unique_eal_name(base_name,folder_path=None):
    import unreal
    import re
    base_part = base_name.partition(".")[0]
    print("The base part is " + base_part)

    delimiter = "_" if "_" in base_part else "-"

    num_match = re.search(rf'(.+?){re.escape(delimiter)}?(\d+)$', base_part)
    print(num_match)
    prefix = base_part

    if num_match:
        prefix = num_match.group(1)
        current_num = num_match.group(2)
        print("current num " + current_num)
        new_num = increment_with_padding(current_num)
        print("The prefix is " + prefix)
        new_base = f"{prefix}{delimiter}{new_num}"
        print("The new base is " + new_base)
    else:
        new_base = f"{base_part}{delimiter}1"
    
    if folder_path:
        final_name = new_base
        counter = 1
        
        while unreal.EditorAssetLibrary.does_asset_exist(f"{folder_path}/{final_name}.{final_name}"):
            new_base = f"{prefix}{delimiter}{counter}"
            final_name = f"{new_base}"
            print("The preview final name is " + final_name)
            counter += 1
        return f"{final_name}.{final_name}"
    return f"{new_base}.{new_base}"

def increment_with_padding(num_str):
    num_length = len(num_str)
    new_num = int(num_str) + 1
    return f"{new_num:0{num_length}d}"