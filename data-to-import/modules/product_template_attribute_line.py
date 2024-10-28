import csv
import os

merged_file_path = r'data-to-import/modules/product_template_attribute_line.xml'
merged_file_path_csv = r'data-to-import/modules/product.template.attribute.line.csv'

# Clear the merged file if it exists
if os.path.exists(merged_file_path):
    open(merged_file_path, 'w', encoding='utf-8').close()  # Clear the file

# Check if the CSV file exists
if os.path.exists('data-to-import/modules/merged_df.csv'):
    with open(r'data-to-import/modules/merged_df.csv', 'r', encoding='utf-8') as file:
        csv_file = list(csv.reader(file))

        # Prepare records to write after the iteration
        records_csv = ['id,product_tmpl_id:id,attribute_id:id,value_ids:id\n']
        records = []
        for line in csv_file[1:]:
            records_csv.append(
                f'{line[7]}_cyl,{line[7]},optic_product_matrix.product_attribute_cyl,optic_product_matrix.{line[5]}\n')
            records_csv.append(
                f'{line[7]}_sph,{line[7]},optic_product_matrix.product_attribute_sph,optic_product_matrix.{line[4]}\n')

            records.append(f"""
<record id="{line[7]}_cyl" model="product.template.attribute.line">
    <field name="product_tmpl_id" ref="{line[7]}"/>
    <field name="attribute_id" ref="optic_product_matrix.product_attribute_cyl"/>
    <field name="value_ids" eval="[(4, ref('optic_product_matrix.{line[5]}'))]"/>
</record>
""")
            records.append(f"""
<record id="{line[7]}_sph" model="product.template.attribute.line">
    <field name="product_tmpl_id" ref="{line[7]}"/>
    <field name="attribute_id" ref="optic_product_matrix.product_attribute_sph"/>
    <field name="value_ids" eval="[(4, ref('optic_product_matrix.{line[4]}'))]"/>
</record>
""")

        # Write CSV records
        with open(merged_file_path_csv, 'a+', encoding='utf-8') as file_to_write:
            file_to_write.writelines(records_csv)

        # Write XML records
        with open(merged_file_path, 'a+', encoding='utf-8') as file_to_write:
            file_to_write.write("""<?xml version="1.0" encoding="utf-8"?>\n<odoo>\n<data>\n""")
            file_to_write.writelines(records)
            file_to_write.write("""</data>\n</odoo>\n""")

else:
    print("File not found!")

print('completed!')
