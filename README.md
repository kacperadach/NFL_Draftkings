## NFL_Draftkings

Python module used to get NFL player scores for Draftkings.

## Requirements

[requests-cache](https://github.com/reclosedev/requests-cache)

## Installation

```bash
pip install NFL_Draftkings
```

## Usage

```python
>> from NFL_Draftkings import get_scores, get_weekly_scores, get_top_performers
>>
>> get_stats(name='Tom Brady', week=1, season=2015)
>> [{u'position': u'QB', u'stats': 27.6, u'name': u'Tom Brady', u'teamAbbr': u'NE'}]
>>
>> get_weekly_scores(name='Tom Brady', weeks=[1,2,3], season=2015)
>> [{'week': 1, u'position': u'QB', u'stats': 27.6, u'name': u'Tom Brady', u'teamAbbr': u'NE'}, 
{'week': 2, u'position': u'QB', u'stats': 32.2, u'name': u'Tom Brady', u'teamAbbr': u'NE'}, 
{'week': 3, u'position': u'QB', u'stats': 25.7, u'name': u'Tom Brady', u'teamAbbr': u'NE'}]
>>
>> get_top_performers(week=1, season=2015, top=5)
>> [{u'position': u'WR', u'stats': 38.1, u'name': u'Julio Jones', u'teamAbbr': u'ATL'}, 
{u'position': u'RB', u'stats': 35.2, u'name': u'Carlos Hyde', u'teamAbbr': u'SF'}, 
{u'position': u'WR', u'stats': 34.6, u'name': u'Keenan Allen', u'teamAbbr': u'SD'}, 
{u'position': u'TE', u'stats': 34.4, u'name': u'Tyler Eifert', u'teamAbbr': u'CIN'}, 
{u'position': u'WR', u'stats': 32.8, u'name': u'DeAndre Hopkins', u'teamAbbr': u'HOU'}] 
```

## Notes

The stats key in the returned dictionaries is the amount of Draftkings points that player scored in the defined period. All methods have position, team, week and season arguments to specify searches as much as needed.

## Updating a pypi module

To update a pypi module version, create a new tag on github with the latest changes you want versioned. After you have pushed the new tag, update setup.py to change the version to that tag number. Then run the following command:

```bash
python setup.py sdist upload
```

This will upload the new version to pypi. If you are having trouble on windows, you need to set the HOME environment variable to where your .pypirc file is located so that you can be authenticated.
