"""Service module 29021: business logic, no crypto."""


def calculate_total_29021(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29021():
    return 'module 29021 handles orders and invoices'
