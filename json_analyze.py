from json import load, loads
from pprint import pprint


class JSONData(object):
    '''A class to contain and analyze JSON data.'''

    def __init__(self, data=None):
        '''(JSONData) -> NoneType

        Create a container and analyzer for JSON data.
        '''
        self.data = data

    def set_data(self, json_data):
        '''(JSONData, list/dict in JSON) -> NoneType

        Set the JSON data for this object to hold.
        '''
        self.data = json_data()

    def get_data(self):
        '''(JSONData) -> list/dict in JSON

        Get the JSON data in list/dict format.
        '''
        return self.data
    
    def _height(self, data):
        '''(JSONData, dict/list in JSON) -> int

        Return the height of the JSON data via recursion.
        '''
        result = 1
        if type(data) in (dict, list):
            # Get a list of all the subheights for data stored in dicts/lists.
            if type(data) is dict:
                subheights = [self._height(data[key]) for key in data.keys()]
            elif type(data) is list:
                subheights = [self._height(element) for element in data]
            # If there is only one height in list, return the only element.
            if len(subheights) == 1:
                result = subheights[0]
            # Otherwise, get and increment the tallest height.
            else:
                result = 1 + max(*subheights)
        # Return the resulting height.
        return result

    def height(self):
        '''(JSONData) -> int

        Return the height (number of levels) of the JSON data.
        '''
        return self._height(self.data)

    def _num_types(self, data):
        '''(JSONData, dict/list in JSON) -> int

        Traverse the JSON data and return a dictionary containing the number
        of items of types dict, list, and str in this data.
        '''
        # Initialize the number values.
        num_dicts, num_lists, num_strs = 0, 0, 0
        # If outer data type is a dict or list, do recursion.
        if type(data) in (dict, list):
            if type(data) is dict:
                num_dicts = 1
                sub_datas = [self._num_types(data[key]) for key in data.keys()]
            elif type(data) is list:
                num_lists = 1
                sub_datas = [self._num_types(element) for element in data]
            # Add up the total number of occurences.
            num_dicts += sum(item[dict] for item in sub_datas)
            num_lists += sum(item[list] for item in sub_datas)
            num_strs += sum(item[str] for item in sub_datas)
        # Otherwise, if type is str, increment num_strs.
        elif type(data) is str:
            num_strs = 1
        # Return the result dictionary.
        return {dict: num_dicts, list: num_lists, str: num_strs}

    def num_types(self):
        '''(JSONData) -> int

        Traverse the JSON data and return a dictionary containing the number
        of items of types dict, list, and str in this data.
        '''
        return self._num_types(self.data)

    def export_to_file(self, file_name):
        '''(JSONData, str) -> NoneType

        Export (write) the JSON data to a file under file_name.
        '''
        print('Exporting to file...', file_name)
        with open(file_name, 'w') as outfile:
            json.dump(json_data, outfile)
        print('Export complete!')


def read_json(json_file_name):
    '''(str) -> JSONData

    Read the JSON data from file name into a JSON data object.
    Return that JSON object.
    '''
    json_file = open(json_file_name, 'r', encoding="utf8")
    json_data = JSONData(loads(json_file.read()))
    json_file.close()
    return json_data


if __name__ == '__main__':
    test = read_json('json_example.json')
