'''
strategy.py
	describes the best strategy to be used by the simulator

Written by Sergio Sanchez
'''

from deck import Rank

# Define the possiblities
S  = 0  # STAND
H  = 1  # HIT
Dh = 2  # DOUBLE (if not allowed, then HIT)
Ds = 3  # DOUBLE (if not allowed, then STAND)
SP = 4  # SPLIT
Sh = 5  # SURRENDER (if not allowed, then HIT)

# from Wikipedia on 04OCT2014 (http://en.wikipedia.org/wiki/Blackjack#Basic_strategy)

basic_strategy_hard = {
# dealer shows rank : { your total is y : your best play is z }
	'2':{ 5:H ,6:H ,7:H ,8:H ,9:H ,10:Dh,11:Dh,12:H ,13:S ,14:S ,15:S ,16:S ,17:S ,18:S ,19:S ,20:S },
	'3':{ 5:H ,6:H ,7:H ,8:H ,9:Dh,10:Dh,11:Dh,12:H ,13:S ,14:S ,15:S ,16:S ,17:S ,18:S ,19:S ,20:S },
	'4':{ 5:H ,6:H ,7:H ,8:H ,9:Dh,10:Dh,11:Dh,12:S ,13:S ,14:S ,15:S ,16:S ,17:S ,18:S ,19:S ,20:S },
	'5':{ 5:H ,6:H ,7:H ,8:H ,9:Dh,10:Dh,11:Dh,12:S ,13:S ,14:S ,15:S ,16:S ,17:S ,18:S ,19:S ,20:S },
	'6':{ 5:H ,6:H ,7:H ,8:H ,9:Dh,10:Dh,11:Dh,12:S ,13:S ,14:S ,15:S ,16:S ,17:S ,18:S ,19:S ,20:S },
	'7':{ 5:H ,6:H ,7:H ,8:H ,9:H ,10:Dh,11:Dh,12:H ,13:H ,14:H ,15:H ,16:H ,17:S ,18:S ,19:S ,20:S },
	'8':{ 5:H ,6:H ,7:H ,8:H ,9:H ,10:Dh,11:Dh,12:H ,13:H ,14:H ,15:H ,16:H ,17:S ,18:S ,19:S ,20:S },
	'9':{ 5:H ,6:H ,7:H ,8:H ,9:H ,10:Dh,11:Dh,12:H ,13:H ,14:H ,15:H ,16:Sh,17:S ,18:S ,19:S ,20:S },
	'T':{ 5:H ,6:H ,7:H ,8:H ,9:H ,10:H ,11:Dh,12:H ,13:H ,14:H ,15:Sh,16:Sh,17:S ,18:S ,19:S ,20:S },
	'J':{ 5:H ,6:H ,7:H ,8:H ,9:H ,10:H ,11:Dh,12:H ,13:H ,14:H ,15:Sh,16:Sh,17:S ,18:S ,19:S ,20:S },
	'Q':{ 5:H ,6:H ,7:H ,8:H ,9:H ,10:H ,11:Dh,12:H ,13:H ,14:H ,15:Sh,16:Sh,17:S ,18:S ,19:S ,20:S },
	'K':{ 5:H ,6:H ,7:H ,8:H ,9:H ,10:H ,11:Dh,12:H ,13:H ,14:H ,15:Sh,16:Sh,17:S ,18:S ,19:S ,20:S },
	'A':{ 5:H ,6:H ,7:H ,8:H ,9:H ,10:H ,11:H ,12:H ,13:H ,14:H ,15:H ,16:Sh,17:S ,18:S ,19:S ,20:S }
}

basic_strategy_soft = {
# dealer shows rank : { your total is y : your best play is z }
	'2':{ 2:H ,3:H ,4:H ,5:H ,6:H ,7:S ,8:S ,9:S },
	'3':{ 2:H ,3:H ,4:H ,5:H ,6:Dh,7:Ds,8:S ,9:S },
	'4':{ 2:H ,3:H ,4:Dh,5:Dh,6:Dh,7:Ds,8:S ,9:S },
	'5':{ 2:Dh,3:Dh,4:Dh,5:Dh,6:Dh,7:Ds,8:S ,9:S },
	'6':{ 2:Dh,3:Dh,4:Dh,5:Dh,6:Dh,7:Ds,8:S ,9:S },
	'7':{ 2:H ,3:H ,4:H ,5:H ,6:H ,7:S ,8:S ,9:S },
	'8':{ 2:H ,3:H ,4:H ,5:H ,6:H ,7:S ,8:S ,9:S },
	'9':{ 2:H ,3:H ,4:H ,5:H ,6:H ,7:H ,8:S ,9:S },
	'T':{ 2:H ,3:H ,4:H ,5:H ,6:H ,7:H ,8:S ,9:S },
	'J':{ 2:H ,3:H ,4:H ,5:H ,6:H ,7:H ,8:S ,9:S },
	'Q':{ 2:H ,3:H ,4:H ,5:H ,6:H ,7:H ,8:S ,9:S },
	'K':{ 2:H ,3:H ,4:H ,5:H ,6:H ,7:H ,8:S ,9:S },
	'A':{ 2:H ,3:H ,4:H ,5:H ,6:H ,7:H ,8:S ,9:S }
}

basic_strategy_pair = {
# dealer shows rank : { your pair is of y : your best play is z }
	'2':{ '2':SP,'3':SP,'4':SP,'5':SP,'6':SP,'7':SP,'8':H ,'9':H ,'T':H ,'J':H ,'Q':H ,'K':H ,'A':H  },
	'3':{ '2':SP,'3':SP,'4':SP,'5':SP,'6':SP,'7':SP,'8':H ,'9':H ,'T':H ,'J':H ,'Q':H ,'K':H ,'A':H  },
	'4':{ '2':H ,'3':H ,'4':H ,'5':SP,'6':SP,'7':H ,'8':H ,'9':H ,'T':H ,'J':H ,'Q':H ,'K':H ,'A':H  },
	'5':{ '2':Dh,'3':Dh,'4':Dh,'5':Dh,'6':Dh,'7':Dh,'8':Dh,'9':Dh,'T':H ,'J':H ,'Q':H ,'K':H ,'A':H  },
	'6':{ '2':SP,'3':SP,'4':SP,'5':SP,'6':SP,'7':H ,'8':H ,'9':H ,'T':H ,'J':H ,'Q':H ,'K':H ,'A':H  },
	'7':{ '2':SP,'3':SP,'4':SP,'5':SP,'6':SP,'7':SP,'8':H ,'9':H ,'T':H ,'J':H ,'Q':H ,'K':H ,'A':H  },
	'8':{ '2':SP,'3':SP,'4':SP,'5':SP,'6':SP,'7':SP,'8':SP,'9':SP,'T':SP,'J':SP,'Q':SP,'K':SP,'A':SP },
	'9':{ '2':SP,'3':SP,'4':SP,'5':SP,'6':SP,'7':S ,'8':SP,'9':SP,'T':S ,'J':S ,'Q':S ,'K':S ,'A':S  },
	'T':{ '2':S ,'3':S ,'4':S ,'5':S ,'6':S ,'7':S ,'8':S ,'9':S ,'T':S ,'J':S ,'Q':S ,'K':S ,'A':S  },
	'J':{ '2':S ,'3':S ,'4':S ,'5':S ,'6':S ,'7':S ,'8':S ,'9':S ,'T':S ,'J':S ,'Q':S ,'K':S ,'A':S  },
	'Q':{ '2':S ,'3':S ,'4':S ,'5':S ,'6':S ,'7':S ,'8':S ,'9':S ,'T':S ,'J':S ,'Q':S ,'K':S ,'A':S  },
	'K':{ '2':S ,'3':S ,'4':S ,'5':S ,'6':S ,'7':S ,'8':S ,'9':S ,'T':S ,'J':S ,'Q':S ,'K':S ,'A':S  },
	'A':{ '2':SP,'3':SP,'4':SP,'5':SP,'6':SP,'7':SP,'8':SP,'9':SP,'T':SP,'J':SP,'Q':SP,'K':SP,'A':SP }
}
