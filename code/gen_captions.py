import pandas as pd

# Load the Excel file
file_path = "C:\\Users\\mehal\\Downloads\\results.csv\\results.csv"  # Update this to the path of your Excel file
  # Update this to the path of your CSV file
df = pd.read_csv(file_path)

# Function to extract text after the last pipe '|'
def extract_caption(text):
    if '|' in text:
        return text.split('|')[-1].strip()
    return text  # Return the original text if no pipe is found

# Assume the captions are in a column named 'Column1'
# Update 'Column1' to the name of your column if it's different
df['Extracted Caption'] = df['Column1'].apply(extract_caption)

# Save the results to a new CSV file
output_path_csv = 'updated_file.csv'  # Update this to your desired output file name
df.to_csv(output_path_csv, index=False)

# Optionally, save the results to a new Excel file
output_path_excel = 'updated_file.xlsx'
df.to_excel(output_path_excel, index=False)

print(f"Processed data has been saved to {output_path_csv} and {output_path_excel}")