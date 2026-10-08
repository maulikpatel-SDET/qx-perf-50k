"""Service module 46586: business logic, no crypto."""


def calculate_total_46586(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46586():
    return 'module 46586 handles orders and invoices'
