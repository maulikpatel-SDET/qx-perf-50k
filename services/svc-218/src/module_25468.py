"""Service module 25468: business logic, no crypto."""


def calculate_total_25468(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25468():
    return 'module 25468 handles orders and invoices'
