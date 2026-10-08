"""Service module 24361: business logic, no crypto."""


def calculate_total_24361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24361():
    return 'module 24361 handles orders and invoices'
