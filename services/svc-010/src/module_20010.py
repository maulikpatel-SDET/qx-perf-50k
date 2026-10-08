"""Service module 20010: business logic, no crypto."""


def calculate_total_20010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20010():
    return 'module 20010 handles orders and invoices'
