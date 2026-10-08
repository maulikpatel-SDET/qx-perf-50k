"""Service module 11720: business logic, no crypto."""


def calculate_total_11720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11720():
    return 'module 11720 handles orders and invoices'
