"""Service module 20660: business logic, no crypto."""


def calculate_total_20660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20660():
    return 'module 20660 handles orders and invoices'
