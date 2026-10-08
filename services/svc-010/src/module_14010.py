"""Service module 14010: business logic, no crypto."""


def calculate_total_14010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14010():
    return 'module 14010 handles orders and invoices'
