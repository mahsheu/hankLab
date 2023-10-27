import gpxpy
import csv

def gpx_to_csv(input_file, output_file):
    with open(input_file, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Latitude', 'Longitude', 'Elevation', 'Time'])

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    csv_writer.writerow([point.latitude, point.longitude, point.elevation, point.time])

if __name__ == "__main__":
    input_gpx_file = "Walk_1_Megan_Lorenz.gpx"
    output_csv_file = "Walk_1_Megan_Lorenz.csv"
    gpx_to_csv(input_gpx_file, output_csv_file)
    print(f"Conversion complete. CSV file saved as '{output_csv_file}'")