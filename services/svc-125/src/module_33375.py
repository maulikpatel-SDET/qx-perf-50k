"""Service module 33375: business logic, no crypto."""


def calculate_total_33375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33375():
    return 'module 33375 handles orders and invoices'
