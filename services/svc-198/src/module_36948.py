"""Service module 36948: business logic, no crypto."""


def calculate_total_36948(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36948():
    return 'module 36948 handles orders and invoices'
