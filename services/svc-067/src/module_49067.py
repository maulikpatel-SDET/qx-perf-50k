"""Service module 49067: business logic, no crypto."""


def calculate_total_49067(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49067():
    return 'module 49067 handles orders and invoices'
