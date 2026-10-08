"""Service module 4713: business logic, no crypto."""


def calculate_total_4713(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4713():
    return 'module 4713 handles orders and invoices'
