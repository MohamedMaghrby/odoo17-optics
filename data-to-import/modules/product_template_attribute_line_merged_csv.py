import pandas as pd


def transform_to_attribute_line_format(file_path, output_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Initialize lists to build the resulting DataFrame
    product_tmpl_ids, attribute_ids, value_ids_list = [], [], []

    # Define attribute identifiers
    attribute_map = {
        'cylinder': 'optic_product_matrix.product_attribute_cyl',
        'sphere': 'optic_product_matrix.product_attribute_sph'
    }

    # Process cylinder and sphere attributes
    for attribute_col, attribute_id in attribute_map.items():
        # Group by product_tmpl_id and collect unique values for each attribute type
        grouped = df.groupby('id')[attribute_col].unique()

        # Append each product attribute line to lists
        for product_tmpl_id, values in grouped.items():
            product_tmpl_ids.append(product_tmpl_id)
            attribute_ids.append(attribute_id)
            value_ids_list.append(",".join([f"optic_product_matrix.{val}" for val in values if pd.notna(val)]))

    # Create the resulting DataFrame
    transformed_df = pd.DataFrame({
        'id': [f"{prod}_{attr.split('.')[-1]}" for prod, attr in zip(product_tmpl_ids, attribute_ids)],
        'product_tmpl_id:id': product_tmpl_ids,
        'attribute_id:id': attribute_ids,
        'value_ids:id': value_ids_list
    })

    # Save the transformed DataFrame to a CSV file
    transformed_df.to_csv(output_path, index=False)


# File paths
input_file_path = '/path/to/your/merged_df.csv'
output_file_path = '/path/to/your/transformed_attribute_lines.csv'

# Run the transformation
transform_to_attribute_line_format(input_file_path, output_file_path)
