"""Service module 12454: business logic, no crypto."""


def calculate_total_12454(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12454():
    return 'module 12454 handles orders and invoices'
