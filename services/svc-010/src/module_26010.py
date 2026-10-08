"""Service module 26010: business logic, no crypto."""


def calculate_total_26010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26010():
    return 'module 26010 handles orders and invoices'
