# coding=gbk
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
# author: Jason  Zeng

def bayes(stock_name):
    plate_df = pd.read_csv('../data_get_deposit/ҽ����е�����ǵ�_pr.csv')  # ��ȡ���ָ�����ļ�
    df = pd.read_csv(f'../data_get_deposit/{stock_name}_pr.csv')  # ��ȡ�������ݵ��ļ�

    up = 0  # ������ǵĴ���
    same = 0  # ��鲻�ǲ����Ĵ���
    down = 0  # ����µ��Ĵ���

    up1 = 0  # �������ǵĴ���
    same1 = 0  # ���ɲ��ǲ����Ĵ���
    down1 = 0  # �����µ��Ĵ���

    up2 = 0  # �������ǵ�ǰ���°�����ǵĴ���
    up3 = 0  # ���ɲ��ǲ�����ǰ���°�����ǵĴ���
    up4 = 0  # �����µ���ǰ���°�����ǵĴ���

    for i in range(len(plate_df)):
        if plate_df.�ǵ���[i] > 0:  # ���ָ������
            up += 1
        elif plate_df.�ǵ���[i] == 0:  # ���ָ�����ǲ���
            same += 1
        elif plate_df.�ǵ���[i] < 0:  # ���ָ���µ�
            down += 1

    # ��P(A) ҽ����е������ǵĸ���
    p_up = up / (i + 1)  # ������ǵĸ���
    print("ҽ����е���������ǵĸ��� P(A)��", p_up)

    # ��P(B) �������ǻ��µ��ĸ���
    for j in range(len(df)):
        if df.�ǵ���[j] > 0:  # ��������
            if plate_df.�ǵ���[j] > 0:
                up2 += 1
            up1 += 1
        elif df.�ǵ���[j] == 0:  # ���ɲ��ǲ���
            if plate_df.�ǵ���[j] > 0:
                up3 += 1
            same1 += 1
        elif df.�ǵ���[j] < 0:  # �����µ�
            if plate_df.�ǵ���[j] > 0:
                up4 += 1
            down1 += 1
    p_up1 = up1 / (j + 1)  # �������ǵĸ���
    p_same1 = same1 / (j + 1)  # ���ɲ��ǲ����ĸ���
    p_down1 = down1 / (j + 1)  # �����µ��ĸ���
    print(f"{stock_name}���ǵĸ��� P(B)��", p_up1)
    print(f"{stock_name}����ĸ��ʣ�", p_same1)
    print(f"{stock_name}�µ��ĸ��ʣ�", p_down1)

    # ��P(A|B=1)����p_up2��ʾ
    p_up2 = up2 / up1
    # ��P(A|B=0)����p_same2��ʾ
    if same1 != 0:
        p_same2 = up3 / same1
    else:
        p_same2 = 0
    # ��P(A|B=-1)����p_down2��ʾ
    p_down2 = up4 / down1

    # P(B|A) = P(A|B)*P(B)/P(A)
    p_up_final = (p_up2 * p_up1) / p_up  # P(B=1|A) = P(A|B)*P(B)/P(A), ��p_same_final��ʾ
    if same1 != 0:
        p_same_final = (p_same2 * p_same1) / p_up   # P(B=0|A) = P(A|B)*P(B)/P(A), ��p_same_final��ʾ
    else:
        p_same_final = 0    # P(B=0|A) = P(A|B)*P(B)/P(A), ��p_same_final��ʾ
    p_down_final = (p_down2 * p_down1) / p_up    # P(B=-1|A) = P(A|B)*P(B)/P(A), ��p_down_final��ʾ
    print(f"{stock_name}����ʱ��������ǵĸ��� P(A|B=1)��", p_up2)
    print(f"{stock_name}����ʱ��������ǵĸ��� P(A|B=0)��", p_same2)
    print(f"{stock_name}�µ�ʱ��������ǵĸ��� P(A|B=-1)��", p_down2)
    print("P(B=1|A) = P(A|B)*P(B)/P(A):", p_up_final)
    print("P(B=0|A) = P(A|B)*P(B)/P(A):", p_same_final)
    print("P(B=-1|A) = P(A|B)*P(B)/P(A):", p_down_final, '\n')
    return p_up_final, p_same_final, p_down_final


if __name__ == '__main__':
    bayes('300760')  # ����ҽ��
    bayes('000652')  # ̩��ɷ�
    bayes('002223')  # ��Ծҽ��
    bayes('002030')  # �ﰲ����
    bayes('600196')  # ����ҽҩ
