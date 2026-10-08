"""Service module 26735: business logic, no crypto."""


def calculate_total_26735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26735():
    return 'module 26735 handles orders and invoices'
