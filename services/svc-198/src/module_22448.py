"""Service module 22448: business logic, no crypto."""


def calculate_total_22448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22448():
    return 'module 22448 handles orders and invoices'
