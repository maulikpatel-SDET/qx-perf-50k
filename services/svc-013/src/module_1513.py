"""Service module 1513: business logic, no crypto."""


def calculate_total_1513(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1513():
    return 'module 1513 handles orders and invoices'
