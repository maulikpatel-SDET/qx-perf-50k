"""Service module 3713: business logic, no crypto."""


def calculate_total_3713(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3713():
    return 'module 3713 handles orders and invoices'
