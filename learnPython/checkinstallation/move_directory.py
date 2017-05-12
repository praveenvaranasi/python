def main():
    import sys
    from .product import Check

    Check.check_product_installation(sys.argv[1])
    pass

if __name__ == '__main__':
    main()
    pass

