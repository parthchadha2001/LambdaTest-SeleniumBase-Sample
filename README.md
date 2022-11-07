
# LambdaTest-SeleniumBase-sample

A guide to run SeleniumBase with LambdaTest

### Prerequisites
- [Download](https://code.visualstudio.com/download) Visual Studio code (IDE) for writing code script
- Install [Python](https://www.python.org/downloads/) on your machine
- Follow the command below to install **virtualenv**
    ```
    pip install virtualenv
    ```
  - For python3 users
  ```
  pip3 install virtualenv
  ```

### Steps to run the test

#### Step 1. Clone the LambdaTest-SeleniumBase-Sample Github repository

```
git clone https://github.com/LambdaTest/LambdaTest-SeleniumBase-Sample.git
```
#### Step 2. Create a virtual environment in your project folder

```
virtualenv venv
```
#### Step 3. Activate the created environment

```
source venv/bin/activate
```
#### Step 4. Install the required packages from the cloned project directory:

```
pip install -r requirements.txt
```
#### Step 5. Set LambdaTest Username and Access Key in environment variables.
 
For Linux/macOS:
```
export LT_USERNAME="YOUR_USERNAME"
export LT_ACCESS_KEY="YOUR ACCESS KEY"
```
For Windows:
```
set LT_USERNAME="YOUR_USERNAME"
set LT_ACCESS_KEY="YOUR ACCESS KEY"
```
### Running the Test
#### Command to execute the SeleniumBase test sample
```
pytest lambdatest.py
```
