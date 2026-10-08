"""Service module 17660: business logic, no crypto."""


def calculate_total_17660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17660():
    return 'module 17660 handles orders and invoices'
