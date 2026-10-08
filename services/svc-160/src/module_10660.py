"""Service module 10660: business logic, no crypto."""


def calculate_total_10660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10660():
    return 'module 10660 handles orders and invoices'
