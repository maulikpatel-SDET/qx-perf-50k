"""Service module 15660: business logic, no crypto."""


def calculate_total_15660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15660():
    return 'module 15660 handles orders and invoices'
