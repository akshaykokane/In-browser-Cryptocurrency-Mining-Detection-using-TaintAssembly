# In-browser Cryptocurrency Mining Detection using TaintAssembly


Website mining has become the alternative revenue generation model.The user gives their computational resources in return of using website service. But mining without the consent of user, is the serious threat and is called cryptojacking. WASM is recently being used on the greater extent for in-browser cryptocurrency mining. Detection of in-browser mining which uses WASM, is the the aim of the project. 
For detection of In-Browser mining, I have used TaintAssembly. You can find more details about taint Assembly over here https://github.com/wfus/WebAssembly-Taint/blob/master/TaintAssembly.pdf


## Getting Started

The project required to work with modified v8 and 64.0.3270.2 version of the chromium.

### Prerequisites

You need to install the depot_tool. For installation follow the instruction from http://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html#_setting_up

```
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH=$PATH:/path/to/depot_tools
```

### Installing

1. Download and follow instrcution for building, compiling and executing the modified V8 from https://github.com/wfus/WebAssembly-Taint
2. Check by V8's in-built debugging tool d8, that modified v8 is working and has the taint_flags. You can find more information about d8 [here](https://v8.dev/docs/d8)
3. Start with fresh directory for checking out the chromium and follow the below steps for icorportating modified v8 in chromium base


```
mkdir ~/chromium && cd ~/chromium
fetch --nohooks chromium
cd src
git checkout 64.0.3270.2
cd v8
git checkout chromium/3270
rm -rf src/
git clone https://www.github.com/wfus/WebAssembly-Taint src/
cd ..
gclient sych
gn gen out/Default

```
This will start the chrome. Verify the chrome and v8 versions are the required one by typing the following in address bar of the chrome

```
chrome://version
```



## Running the chrome in taint mode

After verifying the versions, then close the chrome and start the chrome with following command 

```
 out/Default/chrome --no-sandbox --js-flags=" --wasm_taint --taint_full_log --taint_log=/home/akshay/workspace2/logs/taint_v8.log"

```
This will start chrome in taint mode. Learn mode about the taint mode from [here](https://github.com/wfus/WebAssembly-Taint/blob/master/TaintAssembly.pdf) 
       
      
### Logging and detection


1. Now from the opened chrome go to https://webassembly.org/demo/Tanks/
2. Either keeping chrome alive or closing it, check that if the log file ```taint_v8.log``` is generated. Open the file and check if logs are successfuly generated. 
3. If logs are generated, then you are on the right path. If not, then you need to fix something.

#### Note
    You may need to delete the profile by deleting all the files from ~/.config/chromium/ (this step is useful if you have compiled the chrome before with newer version). Also I got more problems while checkouting the older version, like with sqlite. I reported the bug, check [here](https://bugs.chromium.org/p/chromium/issues/detail?id=906411#) to know more about the bug and fixes

Detection:

1. Copy on your local ```testsite``` 
2. Open testsite/index.html in the chrome
3. This will generate the log file as testsite/index.html has the wasm mining script in it (coinhive)
4. Close the chrome 
5. For detection

```
python detection.py /home/akshay/workspace2/logs/taint_v8.log
```
This should return :
```
DANGER: The Website taint_v8.log was using InBrowser CryptoCurrency Mining
```
if the website doesn't have WASM mining script, then it will return

```
MESSAGE: The Website  taint_v8.log was not using InBrowser CryptoCurrency Mining
```

## Test

The file ```depthallminerstart.txt``` containts the dataset of all the webpages that have mining keyword or coinhive keyword

Run the following command 

```
python testAccuracy.py
```
This will open all the websites from the list for 70s and collect the logs of the websites which uses WASM for mining. Collect the logs and provide the collection logs to ```detection.py``` script to check if it can detect the mining. I tried and got accuracy around 98%.

## Authors
Akshay Kokane
akshaykokane.com


## Acknowledgments

* Thanks to Prof. Kyu Lee, University of Georgia, Athens for guidance.
* Special thanks to  William Fu, Daniel Inge, and Raymond Lin for open sourcing the TaintAssembly (https://github.com/wfus/WebAssembly-Taint).

## References
1. https://chromium.googlesource.com/chromium/src/+/master/docs/linux_build_instructions.md
2. http://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html#_setting_up
3. https://v8.dev/docs/build-gn
