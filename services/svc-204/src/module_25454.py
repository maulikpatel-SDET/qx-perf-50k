"""Service module 25454: business logic, no crypto."""


def calculate_total_25454(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25454():
    return 'module 25454 handles orders and invoices'
