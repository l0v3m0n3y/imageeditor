import requests
class Client():
	def __init__(self):
		self.first_api="https://api.imageeditor.ai"
		self.two_api="https://imageeditor.ai/account/api"
		self.site="https://imageeditor.ai"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def get_result(self,uuid):
		return requests.get(f"{self.site}/conversion/results/{uuid}",headers=self.headers).json()
	def create_conversions(self,terms,model,negative_terms):
		data={"terms":terms,"negative_terms":"","model":model,"dimension":"landscape"}
		if negative_terms:data["negative_terms"]=negative_terms
		return requests.post(f"{self.first_api}/conversions/create/",json=data,headers=self.headers).json()
	def conversions(self,uuid,terms,model,negative_terms):
		data={"terms":terms,"negative_terms":"","model":model,"dimension":"landscape","type":"create","uuid":uuid}
		if negative_terms:data["negative_terms"]=negative_terms
		return requests.post(f"{self.site}/conversion/",json=data,headers=self.headers).json()