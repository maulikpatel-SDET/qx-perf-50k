"""Service module 47865: business logic, no crypto."""


def calculate_total_47865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47865():
    return 'module 47865 handles orders and invoices'
