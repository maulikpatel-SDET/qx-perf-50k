"""Service module 23948: business logic, no crypto."""


def calculate_total_23948(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23948():
    return 'module 23948 handles orders and invoices'
