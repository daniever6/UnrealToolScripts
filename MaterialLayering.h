// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "UObject/ObjectMacros.h"
#include "Materials/MaterialFunctionMaterialLayer.h"
#include "Materials/MaterialLayersFunctions.h"
#include "Materials/MaterialInstanceConstant.h"
#include <stack>
#include <iostream>
#include "MaterialLayering.generated.h"



/**
 * 
 */
UCLASS(BLueprintable)
class MASTERTA_API UMaterialLayering : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
public:
	UFUNCTION(BlueprintCallable, Category = "Material Layers", meta = (DisplayName = "Add Material Layer"))
	static UMaterialInstanceConstant* AddMaterialLayer(UMaterialInstanceConstant* materialInstance, UMaterialFunctionInterface* layerAsset, UMaterialFunctionInterface* blendAsset, FText layerName);

	UFUNCTION(BlueprintCallable, Category = "Material Layers", meta = (DisplayName = "Get Material Layer Info"))
	static void GetMaterialLayersInfo(UMaterialInstanceConstant* materialInstance);
	
	UFUNCTION(BlueprintCallable, meta = (Keywords = "Python Editor"), Category = "PythonEditor")
	static int32 ApplyInstanceChangesToBlueprint(AActor* Actor);

	
};
