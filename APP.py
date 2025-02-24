# 导入需要的库
import streamlit as st
import pandas as pd
import joblib

st.header('基于机器学习的健康人群血浆蛋白质组学衰老预测模型')
st.sidebar.header('变量')

a = st.sidebar.number_input("Pro5（浓度）",value=31.55,step=0.01)
b = st.sidebar.number_input("Pro6（浓度）",value=258.58,step=0.01)
c = st.sidebar.number_input("空腹血糖",value=6.01,step=0.01)
d = st.sidebar.number_input("Pro2（浓度）",value=28.88,step=0.01)
e = st.sidebar.number_input("'Pro3（浓度）",value=709.60,step=0.01)
f = st.sidebar.number_input("Pro1（浓度）",value=163.79,step=0.01)
g = st.sidebar.number_input("总胆固醇",value=5.49,step=0.01)
h = st.sidebar.number_input("收缩压",value=120,step=1)
i = st.sidebar.number_input("饮酒史",value=0,step=1)
j = st.sidebar.number_input("吸烟史",value=0,step=1)

# 如果按下按钮
if st.button("预测"):  # 显示按钮
    # 加载训练好的模型
    model = joblib.load("XGBoost.pkl")
    # 将输入存储DataFrame
    X = pd.DataFrame([[a,b,c,d,e,f,g,h,i,j]],
                     columns = ['Pro5（浓度）', 'Pro6（浓度）', '空腹血糖', 'Pro2（浓度）', 'Pro3（浓度）', 'Pro1（浓度）',
       '总胆固醇', '收缩压', '饮酒史', '吸烟史'])

    # 进行预测
    prediction = model.predict(X)[0]
    Predict_proba = model.predict_proba(X)[:, 1][0]
    # 输出预测结果
    if prediction == 0:
        st.subheader(f"模型预测结果为:  未衰老")
    else:
        st.subheader(f"模型预测结果为:  衰老")
    st.subheader(f"衰老概率为:  {'%.2f' % float(Predict_proba * 100) + '%'}")


