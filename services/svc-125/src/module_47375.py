"""Service module 47375: business logic, no crypto."""


def calculate_total_47375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47375():
    return 'module 47375 handles orders and invoices'
