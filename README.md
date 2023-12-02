# Building a Machine Learning Workflow for Scones Unlimited with Amazon SageMaker

## Project Overview

### Step 1: Data Staging

**Objective:** Extract the CIFAR-100 dataset, transform it, and load it into Amazon S3.

**Execution:**
1. Defined `extract_cifar_data` function in the notebook to download and extract CIFAR-100 dataset from the provided URL.
2. Used tarfile to decompress the dataset and explore its structure.
3. Identified bicycles and motorcycles labels in the dataset.
4. Filtered the dataset for bicycles (label 8) and motorcycles (label 48).
5. Saved the images into the `./train` and `./test` directories.

### Step 2: Model Training and Deployment

**Objective:** Train an image classification model using AWS SageMaker, deploy the model, and set up monitoring.

**Execution:**
1. Generated metadata files (`train.lst` and `test.lst`) for training and testing datasets.
2. Uploaded metadata files to S3.
3. Retrieved the latest image-classification container URI using the SageMaker SDK.
4. Configured and created a SageMaker estimator with ml.p3.2xlarge instance.
5. Set hyperparameters, defined model inputs, and initiated model training.
6. Deployed the model with data capture configured for monitoring.
7. Tested the deployed model with sample images.

### Step 3: Lambdas and Step Function Workflow

**Objective:** Create Lambda functions for data generation, image classification, and inference filtering. Design a Step Function workflow to orchestrate these functions.

**Execution:**
1. Created three Lambda functions: `serializeImageData`, `classifyImage`, and `filterInferences`.
2. Deployed each Lambda function with appropriate permissions.
3. Constructed a Step Function using the visual editor, chaining Lambda invocations.
4. Removed error handling from the last Lambda function for explicit failure.

### Step 4: Testing and Evaluation

**Objective:** Test the Step Function with the test dataset, evaluate results, and monitor model performance.

**Execution:**
1. Generated test cases using the provided `generate_test_case` function.
2. Executed multiple invocations of the Step Function with generated test cases.
3. Extracted and visualized captured data from SageMaker Model Monitor for evaluation.
4. Checked the inferences against a defined confidence threshold.

### Step 5: Cleanup Cloud Resources

**Objective:** Clean up all resources to avoid ongoing costs.

**Execution:**
1. Deleted endpoints, models, and instances used in training and inference.
2. Ensured all associated resources were removed to prevent any unintended charges.

## Additional Files

- **lambda.py:** Contains the code for the Lambda functions.
- **step_function_screenshot.png:** A screenshot of the working Step Function.
- **step_function_definition.json:** The exported JSON file of the Step Function.

## Running the Project

1. Open the provided notebook in an AWS Sagemaker environment.
2. Execute each cell in the notebook sequentially to complete the project steps.
3. Use the generated Lambda functions and Step Function for workflow orchestration.
4. Utilize the test cases and captured data for testing and evaluation.
5. Follow the cleanup steps to avoid ongoing AWS costs.

**Note:** Ensure proper configurations, permissions, and dependencies are set up as outlined in the notebook. Adjustments may be needed based on specific AWS account settings.

## Building a State Machine via AWS Step Functions
* Step Function Graph (that met the inference threshold)
![grapgh](screenshots/Stepfgraph1..png)

* Step Function Graph (that did not meet the inference threshold)
  !![grapgh](screenshots/Stepfgraph2..png)
