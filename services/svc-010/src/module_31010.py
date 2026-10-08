"""Service module 31010: business logic, no crypto."""


def calculate_total_31010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31010():
    return 'module 31010 handles orders and invoices'
