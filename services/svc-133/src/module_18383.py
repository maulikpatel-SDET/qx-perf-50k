"""Service module 18383: business logic, no crypto."""


def calculate_total_18383(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18383():
    return 'module 18383 handles orders and invoices'
