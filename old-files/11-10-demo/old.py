
def initialize(context):
    stocks = ['SZ399305']
    context.set_universe(stocks)


def handle_data(context,o,hsh):
    stat = hsh.bh_getState(es=context.current_dt)
    high = 0
    low = 1
    for pos in context.portfolio.positions:
        if stat == high:
       		o.order(pos.security,10)
		print ('position %s have %d amount' % (pos, pos.total_amount))
   	elif stat == low:
        	o.order(pos.security,10,False)
        	print ('position %s have %d amount' % (pos, pos.total_amount))
    return 0
    
