import json
import time


def count_records(data, count=0):
    """
    Count all the objects AND keys in a JSON structure, EXCEPT for keys
    named "children".
    """
    if isinstance(data, list):
        for record in data:
            if 'children' in record:
                count += count_records(record['children'], count)
                # Count the keys and subtract 1 for the "children" key.
                count += len(record) - 1
            else:
                # Count the keys.
                count += len(record)
            # Count the current record
            count += 1
    else:
        count += count_records(data['children'], count)
        # We're counting the "children" key here, because we're not adding 1
        # for the root record.
        count += len(data)
    return count


def fake_work():
    """Pretend to do some intensive work."""
    time.sleep(0.2)


class FakeImport(object):
    """Process a JSON string, send status updates to `status_callback`"""

    status_callback = lambda completed, total: (completed, total)

    def __init__(self, data, status_callback=None):
        self.data = json.loads(data)
        self.count = count_records(self.data)
        self.processed_records = 0
        if status_callback:
            self.callback = status_callback

        self.import_data()

    def update_status(self):
        self.processed_records += 1
        self.callback(self.processed_records, self.count)

    def process_key(self, key, value):
        if key == 'children':
            self.process_list(value)
        else:
            fake_work()
            self.update_status()

    def process_list(self, data):
        assert isinstance(data, list)
        for record in data:
            self.process_dict(record)

    def process_dict(self, data):
        assert isinstance(data, dict)
        for key, value in data.items():
            self.process_key(key, value)
        fake_work()
        self.update_status()

    def import_data(self):
        print "Processing %s records" % self.count
        if isinstance(self.data, list):
            self.process_list(self.data)
        elif isinstance(self.data, dict):
            self.process_dict(self.data)
        else:
            raise TypeError('Unprocessable Entity %s' % self.data)
        print '\nDONE!'


if __name__ == '__main__':
    from importdata import DATA
    from statusbar import status_bar
    FakeImport(DATA, status_bar)
