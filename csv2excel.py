import csv
import xlsxwriter

def getHeaders(input_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        return headers

def createExcel(csvFile):
    workbook = xlsxwriter.Workbook()
    worksheet = workbook.add_worksheet()

    # Get the header row using the create_header function
    header_row = getHeaders(csvFile)

    # Write the header row to the Excel worksheet
    for c, header in enumerate(header_row):
        worksheet.write(0, c, header)

    with open('convertedFile.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r + 1, c, col)
    workbook.close()

if __name__ == "__main__":
    csvFile = "Walk_1_Megan_Lorenz.csv"
    createExcel(csvFile)
    print(f"Conversion complete. Excel file saved as '{csvFile}'")


# need to make it for any file name
