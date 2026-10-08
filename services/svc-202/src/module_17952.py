"""Service module 17952: business logic, no crypto."""


def calculate_total_17952(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17952():
    return 'module 17952 handles orders and invoices'
