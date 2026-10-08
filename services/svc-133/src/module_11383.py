"""Service module 11383: business logic, no crypto."""


def calculate_total_11383(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11383():
    return 'module 11383 handles orders and invoices'
