import os
import sys
import shutil

PROGRAM_FILES = os.environ["ProgramFiles"]
VISUAL_STUDIO_INSTALLED_VERSION = 2022
VISUAL_STUDIO_INSTALLED_VARIANT = ["Community", "Professional", "Enterprise"]

MS_BUILD_PATH = '{}\\Microsoft Visual Studio\\{}\\{}\\MSBuild\\Current\\Bin\\MSBuild.exe'

for variant in VISUAL_STUDIO_INSTALLED_VARIANT:
    if os.path.exists(
        MS_BUILD_PATH.format(
            PROGRAM_FILES, VISUAL_STUDIO_INSTALLED_VERSION, variant
        )
    ):
        MS_BUILD_PATH = MS_BUILD_PATH.format(
            PROGRAM_FILES, VISUAL_STUDIO_INSTALLED_VERSION, variant
        )
        break

PROJECT_SOLUTION_PATH = os.path.join(os.path.curdir, 'deepinWSL.sln')
MS_BUILD_TARGET = "Build"
MS_BUILD_CONFIG = "Debug"
MS_BUILD_PLATFORM = "x64"

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if sys.argv[i].startswith("--target="):
            MS_BUILD_TARGET = sys.argv[i].split("=")[1].capitalize()
            if MS_BUILD_TARGET == "Clean":
                break
        elif sys.argv[i].startswith("--config="):
            MS_BUILD_CONFIG = sys.argv[i].split("=")[1].capitalize()
        elif sys.argv[i].startswith("--platform="):
            MS_BUILD_PLATFORM = sys.argv[i].split("=")[1]

BUILD_COMMAND = f"\"{MS_BUILD_PATH}\" {PROJECT_SOLUTION_PATH} /t:{MS_BUILD_TARGET} /m /nr:true /p:Configuration={MS_BUILD_CONFIG};Platform={MS_BUILD_PLATFORM}"

exitCode = os.system(BUILD_COMMAND)

if (MS_BUILD_TARGET == "Clean"):
    cleanDirs = [
        "deepinWSL\\x64",
        "deepinWSL\\ARM64",
        "deepinWSL-Appx\\x64",
        "deepinWSL-Appx\\ARM64",
        "deepinWSL-Appx\\BundleArtifacts",
        "x64\\Debug",
        "x64\\Release",
        "AppPackages"
    ]

    cleanFiles = [
        "deepinWSL-Appx\\deepinWSL-Appx.vcxproj.user",
        "deepinWSL\\deepinWSL.vcxproj.user",
        "deepinWSL\\MSG00409.bin",
    ]

    for cleanDir in cleanDirs:
        if os.path.exists(cleanDir):
            shutil.rmtree(cleanDir)

    for cleanFile in cleanFiles:
        if os.path.exists(cleanFile):
            os.remove(cleanFile)

sys.exit(exitCode)
