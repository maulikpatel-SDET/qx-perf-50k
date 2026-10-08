"""Service module 23836: business logic, no crypto."""


def calculate_total_23836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23836():
    return 'module 23836 handles orders and invoices'
