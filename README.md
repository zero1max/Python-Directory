# Python Directory Management

This repository provides examples and explanations on how to work with directories in Python.

## 📂 What You Will Learn
- Getting the current working directory
- Changing directories
- Joining and splitting paths
- Checking if a path is a directory
- Creating, renaming, and deleting directories
- Traversing directories recursively

## 🛠 Requirements
Make sure you have Python installed. You can check your Python version by running:

```sh
python --version
```

## 📌 Usage
Clone the repository and navigate to the project folder:

```sh
git clone https://github.com/yourusername/python-directory.git
cd python-directory
```

## 📜 Code Examples

### 1️⃣ Get the Current Directory
```python
import os

cwd = os.getcwd()
print(cwd)  # Prints the current working directory
```

### 2️⃣ Change the Current Working Directory
```python
import os

os.chdir('/main2')  # Change to /main2 directory
swd = os.getcwd()
print(swd)
```

### 3️⃣ Join and Split a Path
```python
import os

fp = os.path.join('temp', 'python')
print(fp)  # temp\python (on Windows)

pc = os.path.split(fp)
print(pc)  # ('temp', 'python')
```

### 4️⃣ Check If a Path Is a Directory
```python
import os

dir = os.path.join("C:\\", "temp")
print(dir)

if os.path.exists(dir) or os.path.isdir(dir):
    print(f'The {dir} is a directory')
```

### 5️⃣ Create a Directory
```python
import os

dir = os.path.join("C:\\", "temp", "python")
if not os.path.exists(dir):
    os.mkdir(dir)
```

### 6️⃣ Rename a Directory
```python
import os

oldpath = os.path.join("C:\\", "temp", "python")
newpath = os.path.join("C:\\", "temp", "python3")

if os.path.exists(oldpath) and not os.path.exists(newpath):
    os.rename(oldpath, newpath)
    print("'{0}' was renamed to '{1}'".format(oldpath, newpath))
```

### 7️⃣ Delete a Directory
```python
import os

dir = os.path.join("C:\\", "temp", "python")
if os.path.exists(dir):
    os.rmdir(dir)
    print(dir + ' is removed.')
```

### 8️⃣ Traverse a Directory Recursively
```python
import os

path = "c:\\temp"
for root, dirs, files in os.walk(path):
    print("{0} has {1} files".format(root, len(files)))
```

## 🏁 Summary
- Use `os.getcwd()` to get the current working directory.
- Use `os.chdir()` to change the working directory.
- Use `os.mkdir()` to create a new directory.
- Use `os.rename()` to rename a directory.
- Use `os.rmdir()` to remove a directory.
- Use `os.walk()` to list the contents of a directory.

## 📜 License
This project is licensed under the MIT License.

