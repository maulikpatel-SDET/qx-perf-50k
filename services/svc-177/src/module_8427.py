"""Service module 8427: business logic, no crypto."""


def calculate_total_8427(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8427():
    return 'module 8427 handles orders and invoices'
