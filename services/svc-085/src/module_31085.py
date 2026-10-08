"""Service module 31085: business logic, no crypto."""


def calculate_total_31085(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31085():
    return 'module 31085 handles orders and invoices'
