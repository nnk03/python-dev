from deepdiff import DeepDiff

old_config = {
    'A':{
        'A-set': [12, 13, 14]
    }
}

new_config = {
    'A':{
        'A-set': [13, 14, 12]
    }
}

def check_a_set_order( path ):
    return 'A-set' in path

def main():
    print("Hello from deep-diff-example!")
    diffWithOrder = DeepDiff( old_config, new_config )
    print( diffWithOrder.pretty() )

    diffWithoutOrder = DeepDiff( old_config, new_config,ignore_order=True )
    print( diffWithoutOrder.pretty() )

    diffWithParticularOrder = DeepDiff( old_config, new_config, ignore_order_func=check_a_set_order)
    print( diffWithParticularOrder.pretty() )


if __name__ == "__main__":
    main()
