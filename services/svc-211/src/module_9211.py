"""Service module 9211: business logic, no crypto."""


def calculate_total_9211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9211():
    return 'module 9211 handles orders and invoices'
