"""Service module 46810: business logic, no crypto."""


def calculate_total_46810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46810():
    return 'module 46810 handles orders and invoices'
