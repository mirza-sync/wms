import csv
import json
import os


def analyze_orders(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found")
        return None

    try:
        # Load csv
        with open(file_path, newline="") as csvfile:
            data = csv.reader(csvfile)

            # Skip the first row (header)
            next(data)

            total_revenue = 0.0
            sold_item_count = {}

            for i, row in enumerate(data):
                try:
                    sku = row[1].strip()
                    quantity = int(row[2])
                    price = float(row[3])

                    if quantity < 0 or price < 0:
                        raise ValueError("Negative values detected")

                    # Calculate total revenue
                    revenue = (quantity) * (price)
                    total_revenue += revenue

                    # Create new sku key if not exist in dict
                    sold_item_count[sku] = sold_item_count.get(sku, 0) + quantity

                except (ValueError, KeyError, TypeError, AttributeError) as e:
                    print(f"Skipping row {i}: Invalid data ({e})")
                    continue

            # Find best-selling SKU
            best_sku = max(sold_item_count, key=sold_item_count.get)

            result = {
                "total_revenue": round(total_revenue, 2),
                "best_selling_sku": {
                    "sku": best_sku,
                    "total_quantity": sold_item_count[best_sku],
                },
            }
            return result

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    FILENAME = "allsome_interview_test_orders-empty.csv"
    output = analyze_orders(FILENAME)

    if output:
        print(json.dumps(output, indent=2))
