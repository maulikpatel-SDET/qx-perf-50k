"""Service module 31375: business logic, no crypto."""


def calculate_total_31375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31375():
    return 'module 31375 handles orders and invoices'
