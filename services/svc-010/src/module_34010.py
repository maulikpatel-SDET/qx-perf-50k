"""Service module 34010: business logic, no crypto."""


def calculate_total_34010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34010():
    return 'module 34010 handles orders and invoices'
