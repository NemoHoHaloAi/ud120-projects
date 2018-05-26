#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    ### your code goes here

    keep_len = int(len(ages)-0.9*len(ages))

    diffs = [(predictions[i][0] - net_worths[i][0])**2 for i in range(len(predictions))] ### focus the [0]

    dict_diff = {}
    for i in range(len(diffs)):
        print diffs[i]
        print ages[i]
        print net_worths[i]
        dict_diff[diffs[i]] = (ages[i], net_worths[i], diffs[i])

    sort_keys = sorted(dict_diff)[:82]

    cleaned_data = [dict_diff[key] for key in sort_keys]

    return cleaned_data
