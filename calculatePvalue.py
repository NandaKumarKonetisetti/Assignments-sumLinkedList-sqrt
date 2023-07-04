from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return p_value
sample1 = list(map(int,input("Enter values for sample 1").split()))
sample2 = list(map(int,input("Enter values for sample 2").split()))
p_value = perform_hypothesis_test(sample1, sample2)
print("P-value:", p_value)
