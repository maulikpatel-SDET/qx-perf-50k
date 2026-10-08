"""Service module 32010: business logic, no crypto."""


def calculate_total_32010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32010():
    return 'module 32010 handles orders and invoices'
