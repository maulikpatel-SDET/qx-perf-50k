"""Service module 25361: business logic, no crypto."""


def calculate_total_25361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25361():
    return 'module 25361 handles orders and invoices'
