"""Service module 32361: business logic, no crypto."""


def calculate_total_32361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32361():
    return 'module 32361 handles orders and invoices'
