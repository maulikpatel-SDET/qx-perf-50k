"""Service module 36340: business logic, no crypto."""


def calculate_total_36340(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36340():
    return 'module 36340 handles orders and invoices'
