if __name__ == '__main__':
    import sys
    from .product import Check

    Check.check_product_installation(sys.argv[1])
