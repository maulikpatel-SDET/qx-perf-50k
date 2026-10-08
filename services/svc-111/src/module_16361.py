"""Service module 16361: business logic, no crypto."""


def calculate_total_16361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16361():
    return 'module 16361 handles orders and invoices'
