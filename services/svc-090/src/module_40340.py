"""Service module 40340: business logic, no crypto."""


def calculate_total_40340(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40340():
    return 'module 40340 handles orders and invoices'
