"""Service module 38361: business logic, no crypto."""


def calculate_total_38361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38361():
    return 'module 38361 handles orders and invoices'
