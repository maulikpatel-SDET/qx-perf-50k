"""Service module 33269: business logic, no crypto."""


def calculate_total_33269(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33269():
    return 'module 33269 handles orders and invoices'
