vali = {}
df_completo['homepass_move']=None
for kn in tqdm(df_geo['IDENTIFICACION'].unique()):
    df_completo = df_geo.loc[df_geo['IDENTIFICACION']==kn].reset_index()
    if df_completo.shape[0]>1:
        df_completo['indice_s']=df_completo.index
        lista_base = list(df_completo.index)
        base_df = pd.DataFrame(columns=['indice','distancia'])
        for i in lista_base:
            distancias = pd.DataFrame(columns=['indice','distancia'])
            lat1 = df_completo.loc[i,'LATITUD']
            long1 = df_completo.loc[i,'LONGITUD']
            for k in lista_base:
                lat2 = df_completo.loc[k,'LATITUD']
                long2 = df_completo.loc[k,'LONGITUD']
                distancia_k = pd.DataFrame(data={
                    'indice':[k],
                    'distancia':[gpx.geo.haversine_distance(lat1,long1,lat2,long2)]
                })
                distancias=pd.concat([distancias,distancia_k])
            base_df = pd.concat([base_df,distancias])

    ar=np.array(base_df['distancia'])
    if ar[(ar>1)&(ar<30)].size==0:
        res=0
    else:
        res=1
    if len(vali)%10000==0:
        pd.DataFrame(vali.items(),columns=['identificacion','flag']).to_csv("DistanciasFinales.csv",";", index=False)
        
    vali[str(kn)]=res
