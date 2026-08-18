name: Build Kivy APK

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install Dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libffi-dev libssl-dev
        pip install --upgrade buildozer cython

    - name: Build APK with Auto-Accept Licenses
      run: |
        mkdir -p ~/.buildozer/android/platform/android-sdk/licenses
        echo -e "\n89370ced66231929363157f35821a73079b3785e\n5be24544a61b68440d72e18021a15026500f633a\nd56f5187479451eabf01fb78af6dfcb131a6481e\n243308027426141846cb307015d6132be12b3e11\n848152fc94949583d707201fd739d3512b7d4310\n7a93lowe8e6e5a60e0a5c43d81b49f42512f43110" > ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-license
        yes | buildozer --warn_on_root=0 android debug

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: DateConverter-APK
        path: bin/*.apk
