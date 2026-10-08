"""Service module 18948: business logic, no crypto."""


def calculate_total_18948(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18948():
    return 'module 18948 handles orders and invoices'
