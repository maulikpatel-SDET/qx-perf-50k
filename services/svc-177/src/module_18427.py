"""Service module 18427: business logic, no crypto."""


def calculate_total_18427(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18427():
    return 'module 18427 handles orders and invoices'
