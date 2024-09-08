def get_ws_grid_bot_message(data):
    if 'message' in data and data['message'] == 'relistingBot':
        return data['message'] + ' ' + data['symbol']
    return data['message']