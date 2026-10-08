"""Service module 13010: business logic, no crypto."""


def calculate_total_13010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13010():
    return 'module 13010 handles orders and invoices'
