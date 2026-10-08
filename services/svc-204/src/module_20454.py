"""Service module 20454: business logic, no crypto."""


def calculate_total_20454(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20454():
    return 'module 20454 handles orders and invoices'
