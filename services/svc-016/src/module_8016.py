"""Service module 8016: business logic, no crypto."""


def calculate_total_8016(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8016():
    return 'module 8016 handles orders and invoices'
