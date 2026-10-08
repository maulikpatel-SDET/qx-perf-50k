"""Service module 33280: business logic, no crypto."""


def calculate_total_33280(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33280():
    return 'module 33280 handles orders and invoices'
