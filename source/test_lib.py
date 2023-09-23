from lib import print_mean, print_median

def test_print_mean():
    assert print_mean("data_test.csv", "age") == 32

def test_print_median():
    assert print_median("data_test.csv", "age") == 30




if __name__ == "__main__":
    test_mean()
    test_median()
    test_count_variable()