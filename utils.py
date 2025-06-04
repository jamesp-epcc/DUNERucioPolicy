from datetime import datetime

# returns a string representing the year from the metadata
# this uses the core.start_time field by preference, falling
# back to core.end_time and then created_timestamp if not
# present or not a valid timestamp
def get_year_from_metadata(jsondata):
    metadata = jsondata["metadata"]
    timestamp = None
    if 'core.start_time' in metadata:
        try:
            timestamp = int(metadata['core.start_time'])
        except ValueError:
            pass
    if timestamp is None and 'core.end_time' in metadata:
        try:
            timestamp = int(metadata['core.end_time'])
        except ValueError:
            pass
    if timestamp is None and 'created_timestamp' in jsondata:
        try:
            timestamp = int(jsondata['created_timestamp'])
        except ValueError:
            pass
    if timestamp is None:
        return 'None'
    else:
        dt = datetime.utcfromtimestamp(timestamp)
        return str(dt.year)
