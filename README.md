# Kifiya week 12


# Task 1: Data Cleaning from JSON Files

## Overview

In **Task 1**, we developed a data processing pipeline that performs the following operations:

1. **Convert JSON to DataFrame**: JSON files are read and converted into Pandas DataFrames.
2. **Data Cleaning**:
   - **Remove Duplicates**: Identifies and removes any duplicate rows from the dataset.
   - **Handle Missing Values**: Fills missing values using forward and backward filling techniques to ensure the integrity of the data.
   - **Date Conversion**: Columns that contain date-related information are converted into `datetime` objects for consistency.
3. **Data Export**:
   - The cleaned DataFrame is saved as a CSV file, making it easier for further analysis and reporting.
4. **Optional Database Storage**:
   - The cleaned data can also be optionally stored in a PostgreSQL database. The table is created or replaced with each process, and the data is stored efficiently for future querying.

## Process Flow

1. **Input**: JSON files located in a specified directory.
2. **Processing**:
   - Each JSON file is loaded into a DataFrame.
   - The DataFrame undergoes a series of cleaning steps: duplicates are removed, missing values are filled, and date columns are standardized.
3. **Output**:
   - The cleaned data is saved as a CSV file in a designated output folder.
   - Optionally, the cleaned data is stored in a PostgreSQL database for further use in analysis or reporting.

## Features

- **Data Conversion**: Efficiently converts JSON data to a format suitable for further processing.
- **Data Cleaning**: Handles common data issues such as missing values and duplicates.
- **Date Handling**: Automatically converts date columns to the appropriate format for analysis.
- **Logging**: Logs every step of the process, including successes, warnings, and errors, to ensure transparency and easy troubleshooting.
- **Database Integration**: Optionally stores cleaned data in a PostgreSQL database for easy querying and access.

## Log File

All operations are logged to a `logfile.log`, capturing:
- Success messages
- Warnings (e.g., empty DataFrames or missing values)
- Errors (e.g., issues with reading JSON files, or database connection issues)

This log ensures that each step of the cleaning process is tracked and allows for easy identification of any issues that might arise.

## Conclusion

Task 1 provides a comprehensive solution for cleaning and processing JSON data, making it ready for further use, whether that involves saving the data as a CSV file or storing it in a PostgreSQL database for further analysis. The pipeline is designed for scalability and transparency, with clear logging to help track its progress.


# Task 2: Object Detection and Model Evaluation with YOLO

## Overview

In **Task 2**, the focus was on implementing **Object Detection using YOLO (You Only Look Once)**, followed by model evaluation to assess the performance of the detection system. The task involved the following key steps:

1. **Data Augmentation**: Applied various augmentation techniques to artificially increase the dataset size, improving the model's ability to generalize and detect objects in diverse conditions.
   
2. **Object Detection with YOLO**: Utilized the YOLO algorithm for real-time object detection. YOLO is a state-of-the-art deep learning model that is capable of detecting multiple objects in images with high speed and accuracy.
   
3. **Model Evaluation**: After training the YOLO model, we evaluated its performance using various classification metrics, such as precision, recall, and F1-score, across several categories of products.

## Data Augmentation

To enhance the model's ability to generalize, **data augmentation techniques** were applied to the training dataset. These techniques included:
- Rotation
- Flipping
- Scaling
- Cropping

By augmenting the data, we effectively increased the size and variability of the dataset, making the model more robust to different types of real-world inputs.

## Object Detection with YOLO

YOLO (You Only Look Once) was employed for real-time object detection. YOLO is known for its efficiency in detecting objects in images by predicting both the bounding box and the class label in a single pass.

- **Model Architecture**: The YOLO model was trained to detect various objects, such as brochures, cosmetic products, medicine bottles, stethoscopes, syringes, tablet packages, and food.
- **Training**: The model was trained on the augmented dataset to learn to identify these objects across different environments and conditions.

## Model Evaluation

After training the YOLO model, it was evaluated using the **classification report**, which provided metrics like precision, recall, and F1-score for each class. Below are the results from the evaluation:

## Classification Report

| Class              | Precision | Recall | F1-score | Support |
|--------------------|-----------|--------|----------|---------|
| Brochure           | 0.50      | 0.80   | 0.62     | 10      |
| Cosmetic Product   | 0.00      | 0.00   | 0.00     | 6       |
| Medicine Bottle    | 0.00      | 0.00   | 0.00     | 9       |
| Stethoscope        | 0.00      | 0.00   | 0.00     | 1       |
| Syringe            | 0.00      | 0.00   | 0.00     | 0       |
| Tablet Package     | 0.00      | 0.00   | 0.00     | 3       |
| Food               | 0.00      | 0.00   | 0.00     | 5       |

| Metric            | Value  |
|-------------------|--------|
| Micro Average     | 0.47   |
| Macro Average     | 0.07   |
| Weighted Average  | 0.15   |



### Key Observations:
- **Brochure** had the highest performance with a precision of **0.50**, recall of **0.80**, and F1-score of **0.62**.
- The other classes (Cosmetic Product, Medicine Bottle, Stethoscope, etc.) performed poorly, with precision, recall, and F1-scores close to **0.00**.
- The **micro average** precision, recall, and F1-score were **0.47**, **0.24**, and **0.31**, respectively, indicating that while the model was able to detect some objects (like brochures), its overall performance across all classes needed improvement.
- The **macro average** and **weighted average** scores were also low, suggesting a need for further improvements in the model, especially in detecting classes with fewer samples (e.g., Syringe, Stethoscope).

## Challenges and Next Steps

- **Class Imbalance**: Some categories (e.g., Syringe, Stethoscope) had very few samples, leading to poor model performance for those classes.
- **Model Improvement**: The model's performance could be improved by:
  - Collecting more data for underrepresented classes.
  - Fine-tuning hyperparameters or using a pre-trained YOLO model for better accuracy.
  - Exploring additional augmentation techniques to further improve generalization.
- **Evaluation Metrics**: The results show that while certain classes performed well, others struggled. Further model optimization is necessary to balance the precision and recall across all categories.

## Conclusion

**Task 2** focused on implementing and evaluating an object detection model using YOLO. Despite applying data augmentation techniques, the model's performance varied across different product categories. Future improvements could involve gathering more data, fine-tuning the model, and addressing class imbalances to improve detection accuracy across all object categories.



