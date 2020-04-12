import csv

def datToCsv(filename1,filename2):
    with open(filename1) as dat_f, open(filename2,'w') as cs_f:
        csv_writer = csv.writer(cs_f)

        for line in dat_f:
            row = [data.strip() for data in line.split("\t")]
            if len(row) == 3:
                csv_writer.writerow(row)


if __name__ == "__main__":
    datToCsv('user_artists.dat','user_artists_new.csv')

# Input : Tab separated file, DAT file (user_artists.dat)
# Output : CSV file (user_artists_new.csv)