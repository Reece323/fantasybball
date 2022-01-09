def espn_fantasy_pull(leagueid):
    import requests
    import csv
    from datetime import datetime, timedelta
    import locale
    locale.setlocale( locale.LC_ALL, '' )
    currentdate = datetime.now()
    futuredate = currentdate + timedelta(days=7)


    league_id = 1446189898
    year = 2022
    url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/<YEAR>/segments/0/leagues/<ID>" + str(league_id) + "?seasonId=" + str(year)
    url = "https://fantasy.espn.com/apis/v3/games/fba/seasons/2022/segments/0/leagues/1446189898"

    r = requests.get(url,
                    cookies={"swid": "49E5AF83-2903-48E1-8B20-1671BFD9543A",
                            "espn_s2": "AEC5vw3K%2BshMgCs7cF7Mn282%2BJXhHq%2FUItl4a4AV44di46fv4Vkb8ji1ANCzWQqGPGSgg%2BSR%2BKHvPmLyTUeHyUi%2BAHYYKy2OW2M%2BQxXUQtO%2F1DBjVhEeKbRGU%2F3zpCgwV0rGw5rv8QIjUvLcdaODJMgvLtx7St8bdjQ62N97Zn23nKBROHKvvPY5yew61Op%2BmZCYpAWEDrK8AUeZXdQOG3spdttkN4rOTIUzPnCysQZDNvsk2e8dNjo1WzLDdRJtr6WQDAnVFzUWvFXKjawc1You"})
    teamdata = r.json()
    matchups = requests.get(url, params={"view": "mMatchup"}).json()
    # print(matchups)

    teamMap = {}

    for team in teamdata['teams']:
        teamMap[team['id']] = team['location'] + " " + team['nickname']

    player_list = []

    for j in range(len(matchups['teams'])):
        for i in range(len(matchups['teams'][j]['roster']['entries'])):
            player = matchups['teams'][j]['roster']['entries'][i]['playerPoolEntry']['player']['fullName']
            if player[-3:] in ['Jr.', 'Sr.', 'III']:
                player = player[:-4]
            elif player[-3:] == " II":
                player = player[:-3]
            else:
                player = player
            player = player.replace(".","")
            player_list.append(player)
    return player_list
# print(espn_fantasy_pull(1446189898))


# espn_team_pull returns a dictionary of each team in the league as keys and a list of
# players in that league as the values. 
def espn_team_pull():
    import requests
    import csv
    from datetime import datetime, timedelta
    import locale
    locale.setlocale( locale.LC_ALL, '' )
    currentdate = datetime.now()
    futuredate = currentdate + timedelta(days=7)

    url = "https://fantasy.espn.com/apis/v3/games/fba/seasons/2022/segments/0/leagues/1446189898"

    teamdata = requests.get(url).json()
    matchups = requests.get(url, params={"view": "mMatchup"}).json()

    teamMap = {}

    for team in teamdata['teams']:
        teamMap[team['id']] = team['location'] + " " + team['nickname']



    fullMap = {}

    for j in range(len(matchups['teams'])):
        player_list = []
        for i in range(len(matchups['teams'][j]['roster']['entries'])):
            player = matchups['teams'][j]['roster']['entries'][i]['playerPoolEntry']['player']['fullName']
            if player[-3:] in ['Jr.', 'Sr.', 'III']:
                player = player[:-4]
            elif player[-3:] == " II":
                player = player[:-3]
            else:
                player = player
            player = player.replace(".","")
            player_list.append(player)
        fullMap[teamMap[j+1]] = player_list

    return fullMap
# print(espn_team_pull())