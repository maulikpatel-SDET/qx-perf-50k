"""Service module 34361: business logic, no crypto."""


def calculate_total_34361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34361():
    return 'module 34361 handles orders and invoices'
