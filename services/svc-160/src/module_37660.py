"""Service module 37660: business logic, no crypto."""


def calculate_total_37660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37660():
    return 'module 37660 handles orders and invoices'
