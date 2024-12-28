# Day 12 of the 66-Day Python Project Challenge 📅

## Today's Learning Title: Complete Guide to Writing a requirements.txt File

---

### 🎯 What Did I Do?
Today, I got familiar with the `pipreqs` package, which automatically identifies the packages used in a project and writes them into a `requirements.txt` file.  
This makes it easier for anyone downloading the project to install all the required versions.

I also learned how to restrict package versions to ensure specific ones are used.

---

### 🔑 What Did I Learn?

#### Transferring Packages to Another System:
With the `requirements.txt` file, we can easily transfer the necessary packages for a project.

#### Useful Commands:
- `pip freeze | grep <package_name>`: Search for packages.
- `pip freeze | grep -i <package_name>`: Case-insensitive search for packages.

---

#### Installing Packages from requirements.txt:
The command `pip install -r requirements.txt` installs the packages automatically.

---

#### Automatically Generating requirements.txt:
Using the command `pip freeze > requirements.txt`, all packages are written into the `requirements.txt` file.

---

#### Version Naming:
Formats like `post1` are used to indicate minor changes after the main release.

---

#### pipreqs Tool:
This tool automatically detects the packages used and writes them into the `requirements.txt` file.  
However, it cannot scan Jupyter Notebook files.  
To list the packages used in the current project, the following command can be used:  
`pipreqs . --print`

---

#### Restricting Versions:
In the `requirements.txt` file, we can restrict versions as follows:
- `numpy>=1.1.2`: Version 1.1.2 or higher.
- `numpy<=1.1.2`: Version 1.1.2 or lower.
- `numpy>=1.1.2, <2.0`: Versions between 1.1.2 and 2.0.
- `numpy~=1.1.3`: Versions above 1.1.3 but below 1.2.0.
- `numpy!=1.1.3`: Prevent installing version 1.1.3.

---

### ✅ Benefits:
No need to manually write the `requirements.txt` file anymore, and the project can be easily run on different systems.

---

### 🚀 Plan for Tomorrow:
Tomorrow, I plan to learn more about the importance of good software design to make projects more scalable and maintainable.
