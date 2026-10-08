"""Service module 35020: business logic, no crypto."""


def calculate_total_35020(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35020():
    return 'module 35020 handles orders and invoices'
