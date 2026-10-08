"""Service module 11896: business logic, no crypto."""


def calculate_total_11896(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11896():
    return 'module 11896 handles orders and invoices'
