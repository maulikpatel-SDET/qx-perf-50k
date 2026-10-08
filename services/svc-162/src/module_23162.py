"""Service module 23162: business logic, no crypto."""


def calculate_total_23162(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23162():
    return 'module 23162 handles orders and invoices'
