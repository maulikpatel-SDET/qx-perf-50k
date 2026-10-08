"""Service module 11882: business logic, no crypto."""


def calculate_total_11882(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11882():
    return 'module 11882 handles orders and invoices'
