import sys


def find_sid_message(sid_map, wanted_sid):
    """Function to find sid message in 'sid-msg.map' file"""
    sid_message = ''
    for line in sid_map:
        split_line = line.split('||')
        if wanted_sid == split_line[0][:-1]:
            sid_message = split_line[1][1:-1]
            break
    return sid_message


def write_output_line(output_dataset, protocol, port, sid_message):
    """Write the formatted output line in answer dataset"""
    if protocol == 'ip':
        output_dataset.write('0,')
    elif protocol == 'tcp':
        output_dataset.write('1,')
    elif protocol == 'udp':
        output_dataset.write('2,')
    elif protocol == 'icmp':
        output_dataset.write('3,')
    else:
        output_dataset.write('-,')

    output_dataset.write(port+',')
    output_dataset.write(sid_message+'\n')


def main():
    dataset1 = sys.argv[1]
    dataset2 = sys.argv[2]

    # Open input files
    community_rules = open(dataset1, "r")
    sid_map = open(dataset2, "r")
    output_dataset = open("T1p2.txt", "w+")

    # Skip header of dataset1
    for i in range(17):
        next(community_rules)

    for line in community_rules:
        stripped_line = line.strip()
        split_line = stripped_line.split(' ')

        # End file processing
        if len(split_line) == 1:
            break

        # Identify keywords in a line of 'community.rules' file and store wanted fields
        idx = 0
        protocol = ""
        port = ""
        sid_message = ""
        for item in split_line:
            if item == 'alert':
                protocol = split_line[idx+1]
            elif item[:2] == '(m':
                port = split_line[idx-1]
            elif item[:4] == 'sid:':
                sid_split = item.split(':')
                sid = sid_split[1][:-1]
                sid_message = find_sid_message(sid_map, sid)

            idx += 1

        write_output_line(output_dataset, protocol, port, sid_message)

    community_rules.close()
    sid_map.close()
    output_dataset.close()


if __name__ == '__main__':
    main()