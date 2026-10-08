"""Service module 340: business logic, no crypto."""


def calculate_total_340(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_340():
    return 'module 340 handles orders and invoices'
