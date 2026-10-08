"""Service module 30454: business logic, no crypto."""


def calculate_total_30454(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30454():
    return 'module 30454 handles orders and invoices'
