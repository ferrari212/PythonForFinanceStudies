# CODE PYTHON
def initialize(context):
    context.techies = [sid(24), sid(1900), sid(16841)]
    # context.appl = sid (24)
    # context.csco = sid (1900)
    # context.amzn = sid (16841)

def handle_data(context, data):
    if data.can_trade(sid(16841)):
        order_target_percent(sid(16841),1.0)

    # print (data.is_stale(sid(24)))
    # order_target_percent(context.appl,.27)
    # order_target_percent(context.csco,.20)
    # order_target_percent(context.amzn,.53)
