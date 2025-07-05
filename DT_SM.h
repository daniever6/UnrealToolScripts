// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Engine/DataTable.h"
#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "DT_SM.generated.h"


/**
 * 
 */


UENUM(BlueprintType)
enum class EMeshCategory : uint8
{
	Unknown     UMETA(DisplayName = "Unknown"),
	Column      UMETA(DisplayName = "Column"),
	Entrance    UMETA(DisplayName = "Entrance"),
	Wall        UMETA(DisplayName = "Wall"),
	CornerIn     UMETA(DisplayName = "CornerIn"),
	CornerEx     UMETA(DisplayName = "CornerEx"),
	CornerExL      UMETA(DisplayName = "CornerExL"),
	CornerExR     UMETA(DisplayName = "CornerExR"),
	CornerInL      UMETA(DisplayName = "CornerInL"),
	CornerInR      UMETA(DisplayName = "CornerInR")
	
};

UCLASS()
class MASTERTA_API UDT_SM : public UDataTable
{
	
	GENERATED_BODY()

	bool fillDataTable(UStaticMesh SM)
	{
		
		return true;
	}

	UFUNCTION(BlueprintCallable, Category = "Cateogry SM", meta = (DisplayName = "Category SM"))
	static EMeshCategory getCategory(UStaticMesh* SM);

	UFUNCTION(BlueprintCallable, Category = "Mesh|Category",meta = (DisplayName = "Category_name"))
	static FName GetCategoryName(EMeshCategory Category);

	UFUNCTION(BlueprintCallable, Category = "Thumbnails",meta = (DisplayName = "Export Thumbnails"))
	static UTexture2D* SaveThumbnailAsTexture2d(UObject* obj, FString TextureName, FString GamePath);
};
