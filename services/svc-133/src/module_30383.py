"""Service module 30383: business logic, no crypto."""


def calculate_total_30383(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30383():
    return 'module 30383 handles orders and invoices'
