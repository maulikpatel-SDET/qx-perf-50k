"""Service module 35660: business logic, no crypto."""


def calculate_total_35660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35660():
    return 'module 35660 handles orders and invoices'
