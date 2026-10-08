"""Service module 16351: business logic, no crypto."""


def calculate_total_16351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16351():
    return 'module 16351 handles orders and invoices'
