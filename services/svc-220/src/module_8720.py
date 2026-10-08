"""Service module 8720: business logic, no crypto."""


def calculate_total_8720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8720():
    return 'module 8720 handles orders and invoices'
