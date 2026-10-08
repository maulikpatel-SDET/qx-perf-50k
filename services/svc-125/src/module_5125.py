"""Service module 5125: business logic, no crypto."""


def calculate_total_5125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5125():
    return 'module 5125 handles orders and invoices'
