"""Service module 24660: business logic, no crypto."""


def calculate_total_24660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24660():
    return 'module 24660 handles orders and invoices'
