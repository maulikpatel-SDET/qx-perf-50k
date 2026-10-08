"""Service module 49382: business logic, no crypto."""


def calculate_total_49382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49382():
    return 'module 49382 handles orders and invoices'
