#여러 파일에 대한 랜덤샘플링
import pandas as pd
list_number = [1]

for i in list_number :
    #경로설정
    refine = pd.read_csv(f'/a/b/product{i}/product{i}.csv', chunksize = 100000) #청크사이즈 설정

    for idx, chunk in enumerate(refine):
        if idx == 0:
            df = chunk.sample(20)

    df.to_csv(f'sample{i}.csv', encoding = 'utf-8-sig', index = False)
