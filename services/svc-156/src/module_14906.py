"""Service module 14906: business logic, no crypto."""


def calculate_total_14906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14906():
    return 'module 14906 handles orders and invoices'
