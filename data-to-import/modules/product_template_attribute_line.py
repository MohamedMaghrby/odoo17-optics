import csv
import os

merged_file_path = r'data-to-import/modules/product_template_attribute_line.xml'

# Clear the merged file if it exists
if os.path.exists(merged_file_path):
    with open(merged_file_path, 'w', encoding='utf-8') as file_to_clear:
        pass  # This will clear the file

# Check if the CSV file exists
if os.path.exists('data-to-import/modules/merged_df.csv'):
    with open(r'data-to-import/modules/merged_df.csv', 'r', encoding='utf-8') as file:
        csv_file = list(csv.reader(file))

        # Prepare records to write after the iteration
        records = []
        for i, line in enumerate(csv_file[1:]):
            record_cyl = f"""
<record id="{line[7]}_cyl" model="product.template.attribute.line">
    <field name="product_tmpl_id" ref="{line[7]}"/>
    <field name="attribute_id" ref="product_attribute_cyl"/>
    <field name="value_ids" eval="[(4, ref('{line[5]}'))]"/>
</record>
"""
            record_sph = f"""
<record id="{line[7]}_sph" model="product.template.attribute.line">
    <field name="product_tmpl_id" ref="{line[7]}"/>
    <field name="attribute_id" ref="product_attribute_sph"/>
    <field name="value_ids" eval="[(4, ref('{line[4]}'))]"/>
</record>
"""
            records.append(record_cyl)
            records.append(record_sph)

            print(i)  # Print current iteration index

        # Write all records to the file at once
        with open(merged_file_path, 'a+', encoding='utf-8') as file_to_write:
            file_to_write.write("""<?xml version="1.0" encoding="utf-8"?>
<odoo>
<data>
""")
            file_to_write.writelines(records)  # Write all records
            file_to_write.write("""</data>
</odoo>
""")

else:
    print("File not found!")

print('completed!')
