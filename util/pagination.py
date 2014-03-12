# -*- coding: utf-8 -*-
class pagination:

	def __init__(self, page=1, limit=10, total=0):
		self.page = page
		self.limit = limit
		self.total = total
		self.page_total = int((total + limit - 1)/limit)
	
	def num_page(self):
		
		if self.page_total < 1:
			page_list.append(1)
		elif 1< self.page_total < 10:
			page_list = xrange(1, self.page_total + 1)
		else:
			if self.page_total - 5 > self.page:
				if self.page - 5 > 1:
					page_list = xrange(self.page - 5, self.page + 5)
				else:
					page_list = xrange(1, 11)
			else:
				page_list = xrange(self.page_total -10, self.page_total+1)			


		return page_list
