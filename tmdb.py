api_key='c38986c04eeba139e93aae724f375443'
url='https://api.themoviedb.org/3/movie/popular'

final=pd.DataFrame()
for j in range(1,501):
    response=requests.get(f'{url}?api_key={api_key}&language=en-US&page={format(j)}').json()

    popularity=[]
    vote_count=[]
    original_language=[]
    title=[]
    vote_average=[]
    release_date=[]
    overview=[]
    
    
    
    for i in response['results']:
        title.append(i['title'])
        popularity.append(i['popularity'])
        vote_count.append(i['vote_count'])
        original_language.append(i['original_language'])
        vote_average.append(i['vote_average'])
        release_date.append(i['release_date'])
        overview.append(i['overview'])
    
    d={'title':title,'overview':overview,'popularity':popularity,'vote_count':vote_count,'original_language':original_language,'vote_average':vote_average,'release_date':release_date}
    
    df=pd.DataFrame(d)
    
    final = pd.concat([final, df], ignore_index=True)
