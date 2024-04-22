import csv
#Updated 4/22/24

def organize_data(input_file, output_file):
    wifi_data = []
    bluetooth_data = []

    with open(input_file, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for row in csv_reader:
            if len(row) >= 11:
                mac_address = row[0]
                ssid = row[1]
                auth_mode = row[2]
                first_seen = row[3]
                channel = row[4]
                rssi = row[5]
                current_latitude = row[6]
                current_longitude = row[7]
                altitude_meters = row[8]
                accuracy_meters = row[9]
                wifi_type = row[10]

                if 'BLE' in ssid:
                    ssid = 'BLUETOOTH'
                if wifi_type == 'WIFI':
                    wifi_data.append([ssid, mac_address, auth_mode, wifi_type, first_seen, channel, rssi,
                                      current_latitude, current_longitude, altitude_meters, accuracy_meters])
                elif wifi_type == 'BLE':
                    bluetooth_data.append([ssid, mac_address, auth_mode, wifi_type, first_seen, channel, rssi,
                                           current_latitude, current_longitude, altitude_meters, accuracy_meters])


    with open(output_file, 'a') as file:
        file.write("Wi-Fi Networks:\n")
        file.write(f"{'SSID':<20} {'MAC':<20} {'AuthMode':<20} {'Type':<20} {'FirstSeen':<20} {'Channel':<20} {'RSSI':<20} {'CurrentLatitude':<20} {'CurrentLongitude':<20} {'AltitudeMeters':<20} {'AccuracyMeters':<20}\n")
        for row in wifi_data:
            file.write(f"{row[0]:<20} {row[1]:<20} {row[2]:<20} {row[3]:<20} {row[4]:<20} {row[5]:<20} {row[6]:<20} {row[7]:<20} {row[8]:<20} {row[9]:<20} {row[10]:<20}\n")
        file.write("\nBLE Networks:\n")
        file.write(f"{'SSID':<20} {'MAC':<20} {'AuthMode':<20} {'Type':<20} {'FirstSeen':<20} {'Channel':<20} {'RSSI':<20} {'CurrentLatitude':<20} {'CurrentLongitude':<20} {'AltitudeMeters':<20} {'AccuracyMeters':<20}\n")
        for row in bluetooth_data:
            file.write(f"{row[0]:<20} {row[1]:<20} {row[2]:<20} {row[3]:<20} {row[4]:<20} {row[5]:<20} {row[6]:<20} {row[7]:<20} {row[8]:<20} {row[9]:<20} {row[10]:<20}\n")

organize_data(r'Output CSV', r'Input TXT')
