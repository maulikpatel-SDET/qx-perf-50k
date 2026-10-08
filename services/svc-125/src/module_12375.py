"""Service module 12375: business logic, no crypto."""


def calculate_total_12375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12375():
    return 'module 12375 handles orders and invoices'
