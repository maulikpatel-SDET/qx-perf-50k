"""Service module 5361: business logic, no crypto."""


def calculate_total_5361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5361():
    return 'module 5361 handles orders and invoices'
