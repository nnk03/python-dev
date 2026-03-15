from deepdiff import DeepDiff

old_config = {
    'A': {
        'A-set': [12, 13, 14],
        'B-set': [12, 13, 14]
    }
}

new_config = {
    'A': {
        'A-set': [13, 14, 12], # Order changed, should report a diff
        'B-set': [13, 14, 12], # Order changed, should be ignored
    }
}

def check_a_set_order(level):
    # If 'A-set' is in the path, return False (do NOT ignore order)
    # For everything else (like B-set), return True (ignore order)
    print(level.path(),'--> ignore order : ', 'A-set' not in level.path())
    return 'A-set' not in level.path()

def main():
    # diffWithOrder = DeepDiff( old_config, new_config )
    # print( diffWithOrder.pretty() )
    #
    # diffWithoutOrder = DeepDiff( old_config, new_config,ignore_order=True )
    # print( diffWithoutOrder.pretty() )

    # ignore_order_func tells DeepDiff WHERE to ignore order.
    # We want it to ignore order ONLY if it's NOT A-set.
    diff = DeepDiff(old_config, new_config, ignore_order_func=check_a_set_order)
    
    print(diff.pretty())

if __name__ == "__main__":
    main()
