import sender_stand_request

def new_order():
    new_order_response = sender_stand_request.create_order()
    track_id = '?t=' + str(new_order_response.json()['track'])
    return track_id

def get_order_status():
    track = new_order()
    order_status = sender_stand_request.get_order(track)
    assert order_status.status_code == 200
    assert order_status.json()["order"] != ""
    #print(order_status.json()['order'])

def test_post_new_order():
    get_order_status()