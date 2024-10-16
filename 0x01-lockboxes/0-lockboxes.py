#!/usr/bin/python3
"""0. Lockboxes"""


def look_next_opened(open_boxes):
    """looks for the next opened box"""
    for index, box in open_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Checks if all boxes can be opened"""
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    auxi = {}
    auxi[0] = {
        'status': 'opened',
        'keys': boxes[0],
    }

    while len(auxi) != len(boxes):
        keys = look_next_opened(auxi)
        if keys:
            for key in keys:
                try:
                    if auxi.get(key) and\
                      auxi.get(key).get('status') == 'opened/checked':
                        continue
                    auxi[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in auxi.values()]:
            continue
        else:
            return False

    return len(auxi) == len(boxes)


def main():
    """Entry point of the system"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
