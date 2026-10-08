"""Service module 21948: business logic, no crypto."""


def calculate_total_21948(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21948():
    return 'module 21948 handles orders and invoices'
