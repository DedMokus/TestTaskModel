import pandas as pd
from catboost import Pool, CatBoostClassifier
from sklearn.metrics import ndcg_score

test = pd.read_csv("test_df.csv", index_col=False)
train = pd.read_csv("train_df.csv", index_col=False)

X_train = train.drop(columns=['target'])
Y_train = train["target"]
X_test = test.drop(columns=['target'])
Y_test = test['target']

train_group_id = X_train['search_id']
test_group_id = X_test['search_id']

train_pool = Pool(X_train,Y_train,group_id=train_group_id)
test_pool = Pool(X_test,Y_test,group_id=test_group_id)

best_model = CatBoostClassifier(
    iterations=100,
    depth=6,
    random_strength=1.01,
    scale_pos_weight=0.75,
    devices='0'
)

best_model.fit(train_pool, eval_set=test_pool)

best_model.save_model("model", format="cbm")


