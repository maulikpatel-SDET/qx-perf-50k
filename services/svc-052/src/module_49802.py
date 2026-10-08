"""Service module 49802: business logic, no crypto."""


def calculate_total_49802(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49802():
    return 'module 49802 handles orders and invoices'
