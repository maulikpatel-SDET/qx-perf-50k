"""Service module 2315: business logic, no crypto."""


def calculate_total_2315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2315():
    return 'module 2315 handles orders and invoices'
