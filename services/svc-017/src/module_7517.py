"""Service module 7517: business logic, no crypto."""


def calculate_total_7517(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7517():
    return 'module 7517 handles orders and invoices'
