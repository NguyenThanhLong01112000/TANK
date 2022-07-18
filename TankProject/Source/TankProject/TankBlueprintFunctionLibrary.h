// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include <Runtime/Core/Public/Misc/FileHelper.h>
#include "TankBlueprintFunctionLibrary.generated.h"

/**
 * 
 */
UCLASS()
class TANKPROJECT_API UTankBlueprintFunctionLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

		UFUNCTION(BlueprintCallable, Category = "File I/O")
		static FString LoadFileToString(FString filename);
};
