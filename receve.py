# -*- coding: UTF-8 -*-
import requests
import json

def main():
    results = ''
    repogitories = requests.get('https://api.github.com/user/repos?access_token=77ac3db89c9fe8090f6260987b726c3cddedcdb2')
    for repogitory in repogitories.json():
        pullrequests = requests.get('https://api.github.com/repos/' + repogitory["full_name"] + '/pulls?access_token=77ac3db89c9fe8090f6260987b726c3cddedcdb2')
        for pullrequest in pullrequests.json():
            results += pullrequest["url"] + ", updated_at:" + pullrequest["updated_at"] + '\n'
    post_data = {}
    if len(results) == 0:
        post_data = {'token':'xoxp-217034937635-328274288149-617008709141-6679e46d022bffaec43fa1052d8fcc29','channel':'#test_bot', 'username':'Tatsuguchi', 'text':'openèÛë‘ÇÃPullRequestÇÕÇ»Ç¢ÇÊÅI'}
    else:
        post_data = {'token':'xoxp-217034937635-328274288149-617008709141-6679e46d022bffaec43fa1052d8fcc29','channel':'#test_bot', 'username':'Tatsuguchi', 'text':results}
    requests.post('https://slack.com/api/chat.postMessage',data=post_data)

if __name__== '__main__':
    main()