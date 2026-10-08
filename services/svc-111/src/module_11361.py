"""Service module 11361: business logic, no crypto."""


def calculate_total_11361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11361():
    return 'module 11361 handles orders and invoices'
