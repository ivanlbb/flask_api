# Introduction 
PoC of a REST API Microservice built with Python and Flask. This microservice loads a ML model previously fitted and saved with pickle, and returns the prediction corresponding the data sent via POST call.

The ML model was trained and fitted using the data located at https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data

# Getting Started

- Python 3.10 required
- Create virtual environment python -m venv poc-venv 
- Activate virtual environment .\poc-venv\Scripts\activate
- Install dependencies via requirementes.txt file (pip install -r requirements.txt )



# Build and Test
A Dockerfile is provided to build an image and run a container. It can be tested localy running in a terminal the command "python run.py" and then "python test.py".

Once the service is running, you can also test it sending POST HTTP calls with a third party application like Postman. The service expects a nine elements form-data or a json. These elements has to be named from "1" to "9" with values from 1 to 10.
Each element represents an attribute of a sample as explained in https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.names:

   1. Clump Thickness               1 - 10
   2. Uniformity of Cell Size       1 - 10
   3. Uniformity of Cell Shape      1 - 10
   4. Marginal Adhesion             1 - 10
   5. Single Epithelial Cell Size   1 - 10
   6. Bare Nuclei                   1 - 10
   7. Bland Chromatin               1 - 10
   8. Normal Nucleoli               1 - 10
   9. Mitoses                       1 - 10






