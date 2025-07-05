// Fill out your copyright notice in the Description page of Project Settings.


#include "DT_SM.h"

#include "ObjectTools.h"
#include "AssetRegistry/AssetRegistryModule.h"
#include "UObject/SavePackage.h"

EMeshCategory UDT_SM::getCategory(UStaticMesh* SM)
{
	if (!IsValid(SM))
	{
		return EMeshCategory::Unknown;
	}
	FString meshName = SM->GetName();
	FString path_name = SM->GetPathName();

	if (path_name.Contains("/Columns/") || meshName.Contains("Column"))
		return EMeshCategory::Column;
            
	if (path_name.Contains("/Entrances/") || meshName.Contains("Entrance"))
		return EMeshCategory::Entrance;
            
	if (path_name.Contains("/Walls/") || meshName.Contains("Wall"))
		return EMeshCategory::Wall;

	if (path_name.Contains("/CornerIn/") || meshName.Contains("CornerIn"))
	{
		if (meshName.Contains("CornerInL")) return EMeshCategory::CornerInL;
		if (meshName.Contains("CornerInR")) return EMeshCategory::CornerInR;
		return EMeshCategory::CornerIn;
	}

	if (path_name.Contains("/CornerEx/") || meshName.Contains("CornerEx"))
	{
		if (path_name.Contains("/CornerExL/") || meshName.Contains("CornerExL")) return EMeshCategory::CornerExL;
		if (path_name.Contains("/CornerExR/") || meshName.Contains("CornerExR")) return EMeshCategory::CornerExR;
		return EMeshCategory::CornerEx;
	}

	return EMeshCategory::Unknown;
}

FName UDT_SM::GetCategoryName(EMeshCategory Category)
{
	switch(Category)
	{
	case EMeshCategory::Column:   return "SM_Column";
	case EMeshCategory::Entrance: return "SM_Entrance";
	case EMeshCategory::Wall:     return "SM_Wall";
	case EMeshCategory::CornerEx:   return "SM_CornerEx";
	case EMeshCategory::CornerIn:   return "SM_CornerIn";
	case EMeshCategory::CornerExR:   return "SM_CornerExR";
	case EMeshCategory::CornerExL:   return "SM_CornerExL";
	case EMeshCategory::CornerInL:   return "SM_CornerInL";
	case EMeshCategory::CornerInR:   return "SM_CornerInR";
	default:                      return "SM_Unknown";
	}
}

UTexture2D* UDT_SM::SaveThumbnailAsTexture2d(UObject* obj, FString TextureName, FString GamePath)
{
	int32 pathSeparatorIdx;
	if (TextureName.FindChar('/', pathSeparatorIdx)) {
		// TextureName should not have any path separators in it
		return nullptr;
	}

	FObjectThumbnail* thumb = ThumbnailTools::GenerateThumbnailForObjectToSaveToDisk(obj);
	if (!thumb) {
		return nullptr;
	}

	FString PackageName = GamePath;
	if (!PackageName.EndsWith("/")) {
		PackageName += "/";
	}
	PackageName += TextureName;

	UPackage* Package = CreatePackage(*PackageName);
	Package->FullyLoad();

	UTexture2D* NewTexture = NewObject<UTexture2D>(Package, *TextureName, RF_Public | RF_Standalone | RF_MarkAsRootSet);
	NewTexture->AddToRoot();
	FTexturePlatformData* platformData = new FTexturePlatformData();
	platformData->SizeX = thumb->GetImageWidth();
	platformData->SizeY = thumb->GetImageHeight();
	//platformData->NumSlices = 1;
	platformData->PixelFormat = EPixelFormat::PF_B8G8R8A8;
	NewTexture->SetPlatformData(platformData);

	FTexture2DMipMap* Mip = new FTexture2DMipMap();
	platformData->Mips.Add(Mip);
	Mip->SizeX = thumb->GetImageWidth();
	Mip->SizeY = thumb->GetImageHeight();

	Mip->BulkData.Lock(LOCK_READ_WRITE);
	uint8* TextureData = (uint8*)Mip->BulkData.Realloc(thumb->GetUncompressedImageData().Num() * 4);
	FMemory::Memcpy(TextureData, thumb->GetUncompressedImageData().GetData(), thumb->GetUncompressedImageData().Num());
	Mip->BulkData.Unlock();

	NewTexture->Source.Init(thumb->GetImageWidth(), thumb->GetImageHeight(), 1, 1, ETextureSourceFormat::TSF_BGRA8, thumb->GetUncompressedImageData().GetData());

	NewTexture->UpdateResource();
	Package->MarkPackageDirty();
	FAssetRegistryModule::AssetCreated(NewTexture);

	FSavePackageArgs SaveArgs;
	SaveArgs.TopLevelFlags = EObjectFlags::RF_Public | EObjectFlags::RF_Standalone;
	SaveArgs.SaveFlags = SAVE_NoError;
	SaveArgs.bForceByteSwapping = true;
	FString PackageFileName = FPackageName::LongPackageNameToFilename(PackageName, FPackageName::GetAssetPackageExtension());
	bool bSaved = UPackage::SavePackage(Package, NewTexture, *PackageFileName, SaveArgs);

	return NewTexture;
}
