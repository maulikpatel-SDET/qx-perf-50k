"""Service module 41269: business logic, no crypto."""


def calculate_total_41269(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41269():
    return 'module 41269 handles orders and invoices'
