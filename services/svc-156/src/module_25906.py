"""Service module 25906: business logic, no crypto."""


def calculate_total_25906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25906():
    return 'module 25906 handles orders and invoices'
