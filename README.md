# Order Analyzer

A Python script to calculate total revenue and identify the best-selling SKU from a CSV data.

## Prerequisite

- Python 3

## How to Run

1. Clone the repo:

   ```cmd
   > git clone https://github.com/mirza-sync/wms.git
   ```

2. Open your terminal in the project's directory.

3. Create python virtual environment and activate it:

   ```cmd
   > py -m venv venv
   > venv\Scripts\activate
   ```

4. Run the program:

   ```cmd
   > py main.py
   ```

5. A JSON output will be generated in your terminal:

   ```json
   {
     "total_revenue": 710.0,
     "best_selling_sku": {
       "sku": "SKU-A123",
       "total_quantity": 5
     }
   }
   ```
