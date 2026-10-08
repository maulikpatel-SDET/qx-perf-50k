"""Service module 36660: business logic, no crypto."""


def calculate_total_36660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36660():
    return 'module 36660 handles orders and invoices'
