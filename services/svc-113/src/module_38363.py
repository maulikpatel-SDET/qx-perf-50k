"""Service module 38363: business logic, no crypto."""


def calculate_total_38363(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38363():
    return 'module 38363 handles orders and invoices'
