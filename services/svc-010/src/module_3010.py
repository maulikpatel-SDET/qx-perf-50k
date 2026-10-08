"""Service module 3010: business logic, no crypto."""


def calculate_total_3010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3010():
    return 'module 3010 handles orders and invoices'
