"""Service module 39660: business logic, no crypto."""


def calculate_total_39660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39660():
    return 'module 39660 handles orders and invoices'
