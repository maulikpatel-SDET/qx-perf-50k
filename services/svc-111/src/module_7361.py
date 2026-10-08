"""Service module 7361: business logic, no crypto."""


def calculate_total_7361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7361():
    return 'module 7361 handles orders and invoices'
