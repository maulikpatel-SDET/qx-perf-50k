"""Service module 45280: business logic, no crypto."""


def calculate_total_45280(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45280():
    return 'module 45280 handles orders and invoices'
