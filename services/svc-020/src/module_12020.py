"""Service module 12020: business logic, no crypto."""


def calculate_total_12020(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12020():
    return 'module 12020 handles orders and invoices'
