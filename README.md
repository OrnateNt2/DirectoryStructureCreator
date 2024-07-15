# Directory Structure Creator

A Python-based tool to create directories and files based on a given structure. This repository provides two versions of the tool:
1. **GUI Version**: A graphical interface using `tkinter` that allows users to input directory structures and select the base directory interactively.
2. **Non-GUI Version**: A command-line tool where the directory structure can be hardcoded directly into the script.

## Features

- **GUI Version**:
  - User-friendly interface.
  - Ability to input complex directory structures.
  - Option to select the base directory for structure creation.
  - Real-time feedback on the success or failure of structure creation.

- **Non-GUI Version**:
  - Simplicity and speed for users who prefer command-line tools.
  - Direct input of directory structure within the script.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. 

### Installation

Clone the repository:
```sh
git clone https://github.com/OrnateNt2/DirectoryStructureCreator.git
cd DirectoryStructureCreator
```

### Example Structures
Here are a few examples of directory structures you can use:
## Example 1:
project/  
│  
├── index.html  
├── css/  
│   ├── style.css  
│   └── theme/  
│       ├── dark.css  
│       └── light.css  
├── js/  
│   ├── app.js  
│   ├── lib/  
│   │   ├── utils.js  
│   │   └── api/  
│   │       ├── api.js  
│   │       └── endpoints.js  
├── assets/  
│   ├── images/  
│   │   ├── logo.png  
│   │   └── background/  
│   │       └── bg.jpg  
│   ├── fonts/  
│   │   ├── Arial.ttf  
│   │   └── Verdana.ttf  
└── README.md  

## Example 2:
mega-project/  
│  
├── main.py  
├── config/  
│   ├── config.yaml  
│   ├── logging.conf  
│   └── secrets/  
│       ├── aws.yaml  
│       └── db.yaml  
├── src/  
│   ├── core/  
│   │   ├── __init__.py  
│   │   ├── models.py  
│   │   └── views.py  
│   ├── utils/  
│   │   ├── __init__.py  
│   │   ├── helpers.py  
│   │   ├── validators.py  
│   │   └── formatters.py  
├── tests/  
│   ├── test_core.py  
│   ├── test_utils.py  
│   ├── integration/  
│   │   ├── test_endpoints.py  
│   │   └── test_database.py  
├── docs/  
│   ├── index.md  
│   ├── api/  
│   │   ├── overview.md  
│   │   └── endpoints.md  
│   └── user-guide/  
│       ├── installation.md  
│       ├── usage.md  
└── .gitignore  
