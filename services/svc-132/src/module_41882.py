"""Service module 41882: business logic, no crypto."""


def calculate_total_41882(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41882():
    return 'module 41882 handles orders and invoices'
