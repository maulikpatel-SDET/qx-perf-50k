"""Service module 22363: business logic, no crypto."""


def calculate_total_22363(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22363():
    return 'module 22363 handles orders and invoices'
