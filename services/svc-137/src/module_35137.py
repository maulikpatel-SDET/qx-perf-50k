"""Service module 35137: business logic, no crypto."""


def calculate_total_35137(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35137():
    return 'module 35137 handles orders and invoices'
