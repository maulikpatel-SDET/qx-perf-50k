"""Service module 32354: business logic, no crypto."""


def calculate_total_32354(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32354():
    return 'module 32354 handles orders and invoices'
