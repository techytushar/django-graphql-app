from django.shortcuts import render
import requests
import json 


def index(request):
    context = {"response":"false"}
    url = 'https://api.github.com/graphql'
    headers = {"Authorization" : "token <Github Token>"}
    query = {}

    if(request.method=="POST"):
      
        query["query"]="""{
  user(login:"%s"){
    name
    isCampusExpert
    isHireable
    isDeveloperProgramMember
	  pinnedRepositories(first:6){
      edges{
        node{
          name
          url
          description
          primaryLanguage{
            name
          }
        }
      }
    }
  }
}""" % request.POST["username"]

        data = requests.post(url=url, json=query, headers=headers)
        data = json.loads(data.text)
        context['name'] = data['data']['user']
        context['response'] = "true"
    return render(request,'app/index.html',context)