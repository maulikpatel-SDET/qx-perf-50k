"""Service module 19948: business logic, no crypto."""


def calculate_total_19948(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19948():
    return 'module 19948 handles orders and invoices'
