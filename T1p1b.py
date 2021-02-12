import sys


def main():
    dataset = sys.argv[1]
    records = []
    with open(dataset, 'r') as reader:
        for line in reader:
            try:
                # Find and store wanted fields
                line_split = line.split('.')
                platform_or_language = line_split[1]
                record_type = line_split[2]
                rest_of_line = line_split[3].split('-')
                sub_type = rest_of_line[0]
                variant = rest_of_line[1].split(':')[0]

                # Save the formatted answer line
                records.append(platform_or_language + ',' + record_type + ',' + sub_type + ',' + variant + '\n')
            except IndexError:
                continue
    # Store the answer in output dataset
    output_dataset = open("T1p1b.txt", "w+")
    for i in records:
        output_dataset.write(i)
    output_dataset.close()


if __name__ == '__main__':
    main()
