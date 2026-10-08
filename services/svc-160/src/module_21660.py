"""Service module 21660: business logic, no crypto."""


def calculate_total_21660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21660():
    return 'module 21660 handles orders and invoices'
