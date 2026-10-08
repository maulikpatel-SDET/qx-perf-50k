"""Service module 48660: business logic, no crypto."""


def calculate_total_48660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48660():
    return 'module 48660 handles orders and invoices'
