"""Service module 31125: business logic, no crypto."""


def calculate_total_31125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31125():
    return 'module 31125 handles orders and invoices'
