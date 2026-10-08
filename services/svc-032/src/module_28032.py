"""Service module 28032: business logic, no crypto."""


def calculate_total_28032(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28032():
    return 'module 28032 handles orders and invoices'
