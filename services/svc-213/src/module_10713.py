"""Service module 10713: business logic, no crypto."""


def calculate_total_10713(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10713():
    return 'module 10713 handles orders and invoices'
