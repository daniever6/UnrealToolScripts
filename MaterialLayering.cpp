// Fill out your copyright notice in the Description page of Project Settings.

#include "MaterialLayering.h"


#include "AssetToolsModule.h"
#include "ContentBrowserModule.h"
#include "IContentBrowserSingleton.h"
#include "AssetRegistry/AssetRegistryModule.h"
#include "Factories/BlueprintFactory.h"
#include "Factories/MaterialInstanceConstantFactoryNew.h"
#include "Materials/MaterialFunctionMaterialLayerBlend.h"
#include "UObject/SavePackage.h"
#include "MaterialEditingLibrary.h"
#include "Kismet2/KismetEditorUtilities.h"
using namespace std;


UMaterialInstanceConstant* UMaterialLayering::AddMaterialLayer(UMaterialInstanceConstant* materialInstance,
	UMaterialFunctionInterface* layerAsset, UMaterialFunctionInterface* blendAsset, FText layerName)
{
	//Declaration to get the stack of the layers
	FMaterialLayersFunctions layersFunctions;
	TMicRecursionGuard Guard;
	FSavePackageArgs SaveArgs;
	SaveArgs.SaveFlags = SAVE_NoError;

	

	if (materialInstance==nullptr || layerAsset==nullptr )
	{
		return nullptr
		;
	}

	
	materialInstance->GetMaterialLayers(layersFunctions,Guard);
	
	if (!layersFunctions.Layers[0])
	{
		UMaterialFunctionMaterialLayer* layer = Cast<UMaterialFunctionMaterialLayer>(layerAsset);
		UMaterialFunctionMaterialLayerInstance* layerInstance = Cast<UMaterialFunctionMaterialLayerInstance>(layerAsset);

		if (layer!=nullptr)
		{
			layersFunctions.Layers[0]=layer;
		}
		if (layerInstance!=nullptr)
		{
			layersFunctions.Layers[0]=layerInstance;
		}

		
		//layersFunctions.EditorOnly.LayerGuids[0] = parentBaseGuid;
		layersFunctions.EditorOnly.LayerGuids[0]= FGuid::NewGuid();
		layersFunctions.EditorOnly.LayerLinkStates[0] = EMaterialLayerLinkState::UnlinkedFromParent;
#if WITH_EDITOR
		materialInstance->PreEditChange(nullptr);
#endif
		materialInstance->SetMaterialLayers(layersFunctions);
#if WITH_EDITOR
		materialInstance->PostEditChange();
		materialInstance->MarkPackageDirty();
		materialInstance->UpdateCachedData();
		materialInstance->ForceRecompileForRendering();
#endif
		
		
	}
	
	
	else
	{
		if (blendAsset==nullptr)
		{
			return nullptr;
		}
		UMaterialFunctionMaterialLayer* layer = Cast<UMaterialFunctionMaterialLayer>(layerAsset);
		UMaterialFunctionMaterialLayerInstance* layerInstance = Cast<UMaterialFunctionMaterialLayerInstance>(layerAsset);
		UMaterialFunctionMaterialLayerBlend* blend = (Cast<UMaterialFunctionMaterialLayerBlend>(blendAsset));

		check(layersFunctions.Layers.Num() == layersFunctions.EditorOnly.LayerGuids.Num());
		check(layersFunctions.Layers.Num() == layersFunctions.EditorOnly.LayerLinkStates.Num());

		//la estructura FMaterialLayersFunctions tiene sus propios layers y blends, que son arrays
		//Solo hay que acceder a ello y modificar ese array.
		if (layer!=nullptr)
		{
			layersFunctions.Layers.Add(layer);
		}
		if (layerInstance!=nullptr)
		{
			layersFunctions.Layers.Add(layerInstance);
		}
		layersFunctions.Blends.Add(blend);
		
#if WITH_EDITORONLY_DATA
		layersFunctions.EditorOnly.LayerStates.Add(true);
		layersFunctions.EditorOnly.LayerStates.SetNum(layersFunctions.EditorOnly.LayerStates.Num());
		layersFunctions.EditorOnly.LayerNames.Add(layerName);
		layersFunctions.EditorOnly.LayerNames.SetNum(layersFunctions.EditorOnly.LayerStates.Num());
		layersFunctions.EditorOnly.LayerGuids.Add(FGuid::NewGuid());
		layersFunctions.EditorOnly.RestrictToLayerRelatives.Add(true);
		layersFunctions.EditorOnly.RestrictToBlendRelatives.Add(true);
		layersFunctions.EditorOnly.LayerLinkStates.Add(EMaterialLayerLinkState::UnlinkedFromParent);

#endif
#if WITH_EDITOR
		
		materialInstance->PreEditChange(nullptr);
#endif
		//sino esta vacio, cojo el array layersFunctions e inserto el nuevo layer.
		materialInstance->SetMaterialLayers(layersFunctions);
		UE_LOG(LogTemp, Log, TEXT("He podido insertar la capa"));
#if WITH_EDITOR
		materialInstance->PostEditChange();
		materialInstance->MarkPackageDirty();
		materialInstance->UpdateCachedData();
		materialInstance->ForceRecompileForRendering();
#endif


		
		return materialInstance;
	}
	
	return materialInstance;
}

void UMaterialLayering::GetMaterialLayersInfo(UMaterialInstanceConstant* materialInstance)
{
	if (!materialInstance)
	{
		UE_LOG(LogTemp, Warning, TEXT("Invalid Material Instance!"));
		return;
	}

	FMaterialLayersFunctions layersFunctions;
	if (!materialInstance->GetMaterialLayers(layersFunctions))
	{
		UE_LOG(LogTemp, Warning, TEXT("Failed to get material layers"));
		return;
	}

	for ( TObjectPtr<UMaterialFunctionInterface> layer : layersFunctions.Layers)
	{
		
		if (layer)
		{
			
			
			FString LayerName = layer->GetName();
			FString LayerPath = layer->GetPathName();
			
			
            
			UE_LOG(LogTemp, Display, TEXT("Layer Name: %s"), *LayerName);
			UE_LOG(LogTemp, Display, TEXT("Layer Path: %s"), *LayerPath);
			
		}
		else
		{
			UE_LOG(LogTemp, Warning, TEXT("Null layer encountered!"));
		}
	}
	for (TObjectPtr<UMaterialFunctionInterface> blend : layersFunctions.Blends)
	{
		FString BlendName = blend->GetName();
		FString BlendPath = blend->GetPathName();
		if (blend)
		{
			UE_LOG(LogTemp, Display, TEXT("blend Name: %s"), *BlendName);
			UE_LOG(LogTemp, Display, TEXT("blend Path: %s"), *BlendPath);
		}
		else
		{
			UE_LOG(LogTemp, Warning, TEXT("Invalid blend encountered!"));
		}
	}
}

int32 UMaterialLayering::ApplyInstanceChangesToBlueprint(AActor* Actor)
{
	return FKismetEditorUtilities::ApplyInstanceChangesToBlueprint(Actor);
}

