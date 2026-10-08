"""Service module 10340: business logic, no crypto."""


def calculate_total_10340(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10340():
    return 'module 10340 handles orders and invoices'
