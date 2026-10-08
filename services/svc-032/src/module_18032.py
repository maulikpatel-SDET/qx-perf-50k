"""Service module 18032: business logic, no crypto."""


def calculate_total_18032(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18032():
    return 'module 18032 handles orders and invoices'
