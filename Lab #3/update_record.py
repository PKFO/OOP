record_collection = {
  2548: {
    'albumTitle': 'Slippery When Wet',
    'artist': 'Bon Jovi',
    'tracks': ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    'albumTitle': '1999',
    'artist': 'Prince',
    'tracks': ['1999', 'Little Red Corvette']
  },
  1245: {
    'artist': 'Robert Palmer',
    'tracks': []
  },
  5439: {
    'albumTitle': 'ABBA Gold'
  }
}
def update_records(record, id, property, value):
    if id not in record.keys():
        return record
    if value == '':
      del record[id][property]
    if property != 'tracks' and value != '':
        record[id].update({property:value})
    if property == 'tracks' and value != '':
        record[id][property].append(value) #ได้แล้ว
    return record