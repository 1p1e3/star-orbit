<div align="center">
    <img src="logo.png" alt="star orbit" align="center" style="width: 200px;">
    <h1 align="center">STAR ORBIT</h1>
</div>

<p align="center">
  <br>English | <a href="../README.md">简体中文</a>
</p>

An AI entity for automated API testing, currently in the demo and exploration phase. This is a practice project, and its stability and intelligence are both poor. It has no practical use at the moment.



## Workflow
<p align="center">
  <img src="workflow.png" alt="workflow" />
</p>


## How to Experience
### Run Locally

1. Ensure that your local environment has `Python 3.13`, as this project is based on `Python 3.13` and hasn't been tested with other versions, which may cause compatibility issues.
2. Clone this project to your local machine:
```commandline
git clone https://github.com/1p1e3/star-orbit.git
```
3. Open the project with `Pycharm` or any other IDE, and configure a virtual environment.
4. Install the project dependencies:
```commandline
pip install -r requirements.txt 
```
5. Once installation is complete, start the Flask API service for testing. Run the following command in the project's root directory:
```commandline
python flask_server.py
```
6. Create a Gemini API Key in Google AI Studio (free). After creating it, copy the key and paste it into the following line of code in `core/agent`.py:
```python
def gemini_client():
    # 创建客户端
    client = genai.Client(api_key="your key")
    ...
```
6. Open a new terminal and run the following command:
```commandline
orbit
```
This will start the workflow and automatically complete the API automation tests. The API documentation used for testing is a sample API document provided in the api_docs directory of the project.

7. If you have a JSON formatted API document (must comply with the OpenAPI specification and include detailed descriptions for the fields), you can start the workflow with the following command:
```commandline
orbit "JSON formatted API document's absolute path"
```
For example:
```commandline
orbit C:\api.json
```
8. After the workflow finishes, the HTML test report will be saved in the output directory under the corresponding subdirectory.




