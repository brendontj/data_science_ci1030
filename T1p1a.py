import sys


def main():
    dataset = sys.argv[1]
    records = {}
    used_labels = []
    with open(dataset, 'r') as reader:
        for line in reader:
            try:
                # Try to split a line and store the wanted fields
                line_split = line.split('-')
                label = line_split[0]
                variant = line_split[1]
                label_splited = label.split(':')
                record = label_splited[2].split('.')
                record_type = record[1]
                family = record[2]

                # Build a key
                key = record_type + "." + family

                if key + '-' + variant not in used_labels:
                    # If is a new key...
                    used_labels.append(key + '-' + variant)
                    # Add +1 different variant record with this key
                    if key in records:
                        records[key] += 1
                    else:
                        records[key] = 1

            except IndexError:
                continue

    # Store the answer in output dataset
    output_dataset = open("T1p1a.txt", "w+")
    for k, v in sorted(records.items()):
        output_dataset.write(k + ',' + str(v)+'\n')
        print(k + ',' + str(v))
    output_dataset.close()


if __name__ == '__main__':
    main()