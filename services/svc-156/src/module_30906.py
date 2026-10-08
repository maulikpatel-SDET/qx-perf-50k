"""Service module 30906: business logic, no crypto."""


def calculate_total_30906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30906():
    return 'module 30906 handles orders and invoices'
