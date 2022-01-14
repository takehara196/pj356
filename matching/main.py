# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def clustering():
    use_agents_cols = [
        "id",
        "preference1",
        "preference2",
        "preference3",
        "preference4",
        "preference5",
        "preference6",
        "preference7",
        "preference8",
        "preference9",
        "needs_1",
        "needs_2",
        "needs_3",
        "needs_4",
        "needs_5"
    ]

    use_buyers_cols = [
        "id",
        "preference1",
        "preference2",
        "preference3",
        "preference4",
        "preference5",
        "preference6",
        "preference7",
        "preference8",
        "preference9",
        "needs_1",
        "needs_2",
        "needs_3",
        "needs_4",
        "needs_5"
    ]

    # agentテーブル
    r = np.random.randint(1, 5, (50, 15))
    agent_df = pd.DataFrame(r, columns=use_agents_cols)
    # idに連番付与
    serial_num = pd.RangeIndex(start=1, stop=len(agent_df.index) + 1, step=1)
    agent_df['id'] = serial_num
    agent_df['id'] = 'agent_' + agent_df['id'].astype(str)

    # buyerテーブル
    r = np.random.randint(1, 5, (20, 15))
    buyer_df = pd.DataFrame(r, columns=use_buyers_cols)
    serial_num = pd.RangeIndex(start=1, stop=len(buyer_df.index) + 1, step=1)
    buyer_df['id'] = serial_num
    buyer_df['id'] = 'buyer_' + buyer_df['id'].astype(str)

    # agent, buyerテーブルを結合
    df = pd.concat([agent_df, buyer_df])
    # idカラムをindexに指定
    df = df.set_index("id")

    # データを4クラスに分割、乱数固定
    model_kmeans = KMeans(n_clusters=4, random_state=0)
    # 学習、フィッティング
    model_kmeans.fit(df.values)
    # 学習済みデータの重心点
    # print(model_kmeans.cluster_centers_)
    # 重心点の形状
    # print(model_kmeans.cluster_centers_.shape)
    # 作成したモデルでクラスタリング
    cluster = model_kmeans.predict(df.values)
    df_class = df.copy()
    df_class['クラス'] = cluster
    print(df_class)

    return


def main():
    clustering()


if __name__ == '__main__':
    main()
