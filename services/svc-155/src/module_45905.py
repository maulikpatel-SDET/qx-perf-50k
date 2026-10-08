"""Service module 45905: business logic, no crypto."""


def calculate_total_45905(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45905():
    return 'module 45905 handles orders and invoices'
