"""Service module 17361: business logic, no crypto."""


def calculate_total_17361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17361():
    return 'module 17361 handles orders and invoices'
