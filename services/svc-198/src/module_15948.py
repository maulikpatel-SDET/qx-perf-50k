"""Service module 15948: business logic, no crypto."""


def calculate_total_15948(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15948():
    return 'module 15948 handles orders and invoices'
