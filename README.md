Python based command line utility
======================

[Virtual Optical Serial Analyser (OSA)](http://ec2-3-134-85-47.us-east-2.compute.amazonaws.com) is a basic text command interface of legacy laboratory equipment. It is created using React and Flask framework. It provides basic controls to retrieve an OSA trace within specified limits and display the result on a graph.

## Table of content

- [Installation](#installation)
    - [React](#react)
    - [Flask](#flask)
- [Features](#features)
    - [Continous Feedback](#continous-feedback)
    - [Zoom, Pan, Read Values](#zoom-pan-read-values-from-the-chart)
    - [Plot Persistence](#plot-persistence)
    - [Command Line Interface](#command-line-interface)
    - [Communication Log](#communication-log)
- [REST Endpoints](#rest-endpoints)
- [Acknowledgements](#acknowledgements)
- [Links](#links)

## Installation

Clone this repository :
`git clone https://github.com/tejasvivig29/analyzere_python_commandlineutility.git`

Make sure you have these installed :

- **Python** - Python 3.6.9 or newer


## Running the command line utility
* Navigate inside the analyzere_python_commandlineutility
* Run the .py 

```
cat input | python compute.py 'Threshold' 'Limit'
```
## Example
```
cat input | python compute.py 1000 20000000
```

### Output Screenshots 

![Output](https://github.com/tejasvivig29/analyzere_python_commandlineutility/blob/main/python_utility_screenshot1.JPG)

![Output in case of wrong inputs](https://github.com/tejasvivig29/analyzere_python_commandlineutility/blob/main/python_utility_screenshot2.JPG)

**Caution:** Input file should consists of up to 100 lines of numbers - all decimal numbers between 0.0 and 10,000,000.0 (inclusive)


