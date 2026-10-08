"""Service module 25750: business logic, no crypto."""


def calculate_total_25750(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25750():
    return 'module 25750 handles orders and invoices'
