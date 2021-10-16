# This is a Python script for Searching Shodan.
import requests
import shodan
from shodan import Shodan
from shodan.cli.helpers import get_api_key

# variable to store API key
SHODAN_API_KEY = "2AUJztFnOpTk4RMKuUrfqURnQLfHqom1"
api = shodan.Shodan(SHODAN_API_KEY)


def getShodanData():
    # Wrap the request in a try/ except block to catch errors
    try:
        # Search Shodan
        results = api.search('apache')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
    except shodan.APIError as e:
        print('Error: {}'.format(e))


def lookupHost():
    # Lookup the host
    host = api.host('192.168.0.14')

    # Print general info
    print("""
            IP: {}
            Organization: {}
            Operating System: {}
    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

    # Print all banners
    for item in host['data']:
        print("""
                    Port: {}
                    Banner: {}

            """.format(item['port'], item['data']))


def getAccountProfile():

    # variable to store api url
    api_start = 'https://api.shodan.io/account/profile?key='

    # complete url address
    url = api_start + SHODAN_API_KEY

    # get method of requests module returns the response object
    # json method of response object converts json format data into python format data
    json_data = requests.get(url).json()

    try:
        if json_data['member'] == True:
            # if member found
            member = json_data['member']
            credits_earned = json_data['credits']
            display_name = json_data['display_name']
            created = json_data['created']

            print("Member: ", member)
            print("Credits: ", credits_earned)  # using round method
            print("Display Name: ", display_name)
            print("Created: ", created)

        else:
            # member not found
            print("\tNot a Member.")
    except:
        print("\tException: Unable to access Member Profile")
        print("\tVerify Member Profile")


# def getAPIDetailTemplate():
#
#     # variable to store api url
#     api_start = 'https://stream.shodan.io/shodan/countries/{countries}?key={YOUR_API_KEY}'
#
#     country = 'US'
#
#     # complete url address
#     url = api_start + country + "?key=" + SHODAN_API_KEY
#
#     # get method of requests module returns the response object
#     # json method of response object converts json format data into python format data
#     json_data = requests.get(url).json()
#
#     try:
#         if json_data['member']:
#             # if  found
#             print("\tMember Profile found")
#
#         else:
#             # not found
#             print("\tMember Profile not found")
#
#     except:
#         print("\tException: Unable to access Member Profile")
#         print("\tVerify Member Profile")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # getShodanData()
    # lookupHost()
    # getAccountProfile()
    api = Shodan(SHODAN_API_KEY)

    limit = 500
    counter = 0
    for banner in api.search_cursor('product:mongodb'):
        # Perform some custom manipulations or stream the results to a database
        # For this example, I'll just print out the "data" property
        print(banner['data'])

        # Keep track of how many results have been downloaded so we don't use up all our query credits
        counter += 1
        if counter >= limit:
            break

