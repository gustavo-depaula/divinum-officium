import json,os,sys,time,urllib.request,urllib.error
SP='/tmp/claude-0/-home-user-divinum-officium/d044b1cc-179c-52e7-87f2-339053039f6a/scratchpad/audit'
REPO='gustavo-depaula/divinum-officium'
TOK=os.environ['GITHUB_TOKEN']
def req(method,url,payload=None):
    data=json.dumps(payload).encode() if payload is not None else None
    r=urllib.request.Request(url,data=data,method=method,headers={
      'Authorization':'Bearer '+TOK,'Accept':'application/vnd.github+json',
      'X-GitHub-Api-Version':'2022-11-28','Content-Type':'application/json',
      'User-Agent':'do-ptbr-audit'})
    with urllib.request.urlopen(r) as f: return json.load(f)
which=sys.argv[1]; lo=int(sys.argv[2]); hi=int(sys.argv[3])
issues=json.load(open(os.path.join(SP,which)))
created=[]
outf=os.path.join(SP,'created.jsonl')
for i,it in enumerate(issues):
    if not (lo<=i<hi): continue
    try:
        res=req('POST',f'https://api.github.com/repos/{REPO}/issues',
                {'title':it['title'],'body':it['body'],'labels':it['labels']})
        rec={'number':res['number'],'title':res['title'],'url':res['html_url'],
             'labels':[l['name'] for l in res.get('labels',[])]}
        created.append(rec)
        with open(outf,'a') as fh: fh.write(json.dumps(rec,ensure_ascii=False)+'\n')
        print(f"#{res['number']}  {res['title'][:78]}")
    except urllib.error.HTTPError as e:
        print('FAILED',it['title'][:60],e.code,e.read().decode()[:300]); break
    time.sleep(1.2)
print('created',len(created))
