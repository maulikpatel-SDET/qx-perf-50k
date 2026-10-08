"""Service module 735: business logic, no crypto."""


def calculate_total_735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_735():
    return 'module 735 handles orders and invoices'
