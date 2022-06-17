class SETTINGS:

    HEADER_TOKEN = {'Authorization': 'Bearer keypxnt6JnEf2hYoe'}
    api_key = 'keypxnt6JnEf2hYoe'
    TABLE_NAME = 'FirstTable'

    TABLE_ID = 'appGFLNUsW0Et9DGN'
    LIST_URL = '?maxRecords=3&view=Grid%20view'

    CREATE_TABLE_URL = f'/{TABLE_ID}/{TABLE_NAME}'

    @property
    def get_url(self):
        return f'https://api.airtable.com/v0/{self.TABLE_ID}/{self.TABLE_NAME}'


settings = SETTINGS()