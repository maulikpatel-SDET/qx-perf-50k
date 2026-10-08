"""Service module 47361: business logic, no crypto."""


def calculate_total_47361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47361():
    return 'module 47361 handles orders and invoices'
