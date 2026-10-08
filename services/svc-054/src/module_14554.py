"""Service module 14554: business logic, no crypto."""


def calculate_total_14554(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14554():
    return 'module 14554 handles orders and invoices'
