"""Service module 29348: business logic, no crypto."""


def calculate_total_29348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29348():
    return 'module 29348 handles orders and invoices'
