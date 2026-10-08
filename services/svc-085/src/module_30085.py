"""Service module 30085: business logic, no crypto."""


def calculate_total_30085(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30085():
    return 'module 30085 handles orders and invoices'
