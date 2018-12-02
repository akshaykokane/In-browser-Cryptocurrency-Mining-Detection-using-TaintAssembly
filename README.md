# In-browser Cryptocurrency Mining Detection using TaintAssembly


Website mining has become the alternative revenue generation model.The user gives their computational resources in return of using website service. But mining without the consent of user, is the serious threat and is called cryptojacking. WASM is recently being used on the greater extent for in-browser cryptocurrency mining. Detection of in-browser mining which uses WASM, is the the aim of the project. 
For detection of In-Browser mining, I have used TaintAssembly. You can find more details about taint Assembly over here https://github.com/wfus/WebAssembly-Taint/blob/master/TaintAssembly.pdf


## Getting Started

1. Download and follow instrcution for building, compiling and executing the modified V8 from https://github.com/wfus/WebAssembly-Taint
2. Check by V8's in-built debugging tool d8, that modified v8 is working and has the taint_flags. You can find more information about d8 here : https://v8.dev/docs/d8


### Prerequisites

You need to install the depot_tool. For installation follow the instruction from http://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html#_setting_up

```
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH=$PATH:/path/to/depot_tools
```

### Installing



```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
