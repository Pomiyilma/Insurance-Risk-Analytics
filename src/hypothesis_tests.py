from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency


def run_ttest(group_a, group_b):

    stat, p_value = ttest_ind(
        group_a,
        group_b,
        nan_policy="omit"
    )

    return stat, p_value


def run_chi_square(contingency_table):

    chi2, p_value, dof, expected = chi2_contingency(
        contingency_table
    )

    return chi2, p_value
