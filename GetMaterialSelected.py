import unreal

def getSelectionContectBrowser():#Coger el material seleccionado en el content browser
    EUL = unreal.EditorUtilityLibrary()# Instanciar la clase EditorUtilityLibrary para usar sus funciones
    selectedAssets = EUL.get_selected_assets()# coger todos los assets que estan seleccionados en el content browser
    if selectedAssets == []:
        unreal.log_warning("No hay materiales seleccionados en el content browser")
    selectedMaterials = []# Lista que guarda los materiales seleccionados
    
    for asset in selectedAssets:
        #Se escoge el primer material que se encuentre, si no es un material, se salta
        if(asset.get_class().get_name() == 'MaterialInstanceConstant' or asset.get_class().get_name() == 'Material'):
            selectedMaterials.append(asset)
    return selectedMaterials# Devuelvo la lista de materiales seleccionados

    

    
