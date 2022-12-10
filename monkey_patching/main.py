# editing the module directly at runtime
import requests
import sample_module

def get_sample_data() -> dict:
    return {'user': 'chiara', 'id': 1234}

if __name__ == '__main__':
    print('before', sample_module.get_data())


    # monkey patching: reassing the function to sample_module
    sample_module.get_data = get_sample_data
    print('after', sample_module.get_data())