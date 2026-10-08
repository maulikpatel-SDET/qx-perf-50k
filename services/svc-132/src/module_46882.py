"""Service module 46882: business logic, no crypto."""


def calculate_total_46882(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46882():
    return 'module 46882 handles orders and invoices'
