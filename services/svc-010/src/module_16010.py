"""Service module 16010: business logic, no crypto."""


def calculate_total_16010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16010():
    return 'module 16010 handles orders and invoices'
