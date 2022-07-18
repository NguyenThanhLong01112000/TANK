// Fill out your copyright notice in the Description page of Project Settings.


#include "TankBlueprintFunctionLibrary.h"
#include <Runtime/Core/Public/Misc/Paths.h>
#include <Runtime/Core/Public/HAL/PlatformFilemanager.h>

FString UTankBlueprintFunctionLibrary::LoadFileToString(FString filename)
{
	FString directory = FPaths::ProjectContentDir();
	FString result;
	IPlatformFile& file = FPlatformFileManager::Get().GetPlatformFile();

	if (file.CreateDirectory(*directory))
	{
		FString myFile = directory + "/" + filename;
		FFileHelper::LoadFileToString(result, *myFile);
	}
	return result;
}
