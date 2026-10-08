"""Service module 19882: business logic, no crypto."""


def calculate_total_19882(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19882():
    return 'module 19882 handles orders and invoices'
