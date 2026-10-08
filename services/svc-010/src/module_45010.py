"""Service module 45010: business logic, no crypto."""


def calculate_total_45010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45010():
    return 'module 45010 handles orders and invoices'
