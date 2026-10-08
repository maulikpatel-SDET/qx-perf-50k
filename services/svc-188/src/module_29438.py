"""Service module 29438: business logic, no crypto."""


def calculate_total_29438(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29438():
    return 'module 29438 handles orders and invoices'
