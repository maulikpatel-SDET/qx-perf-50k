"""Service module 25517: business logic, no crypto."""


def calculate_total_25517(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25517():
    return 'module 25517 handles orders and invoices'
