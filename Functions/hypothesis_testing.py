# hypothesis_testing.py

from scipy.stats import chi2_contingency, mannwhitneyu, norm
import numpy as np

def chi_square_test(observed):
    """Perform chi-square test for independence."""
    chi2, p_value, dof, expected = chi2_contingency(observed)
    return chi2, p_value, dof, expected

def mann_whitney_u_test(control, test):
    """Perform Mann-Whitney U test."""
    u_stat, p_value = mannwhitneyu(control, test)
    return u_stat, p_value

def z_test(control_success, control_total, test_success, test_total):
    """Perform Z-test for proportions."""
    control_prop = control_success / control_total
    test_prop = test_success / test_total
    pooled_prop = (control_success + test_success) / (control_total + test_total)
    se = np.sqrt(pooled_prop * (1 - pooled_prop) * (1/control_total + 1/test_total))
    z_score = (test_prop - control_prop) / se
    p_value = 1 - norm.cdf(z_score)
    return z_score, p_value
