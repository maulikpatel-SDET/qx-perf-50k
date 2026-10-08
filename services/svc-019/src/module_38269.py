"""Service module 38269: business logic, no crypto."""


def calculate_total_38269(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38269():
    return 'module 38269 handles orders and invoices'
