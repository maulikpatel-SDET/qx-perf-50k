"""Service module 2361: business logic, no crypto."""


def calculate_total_2361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2361():
    return 'module 2361 handles orders and invoices'
