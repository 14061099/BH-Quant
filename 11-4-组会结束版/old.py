def initialize(context):
    stocks = ['SZ002680']
    context.set_universe(stocks)


def handle_data(context,o):
    for pos in context.portfolio.positions:
	nowp = o.get_current_price(context.universe[0])
	amnt = 10	
	if o.price[1]<nowp:
	    print context.current_dt.strftime('%H:%M'),('---up(%.2f->%.2f) buy in %d ' % (o.price[1],nowp,amnt))
	    print ('current amount:%d' % context.portfolio.positions[0].total_amount)
            o.order(pos.security, amnt)
    return 0
