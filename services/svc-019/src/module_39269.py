"""Service module 39269: business logic, no crypto."""


def calculate_total_39269(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39269():
    return 'module 39269 handles orders and invoices'
