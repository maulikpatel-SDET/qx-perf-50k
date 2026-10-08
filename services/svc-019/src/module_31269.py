"""Service module 31269: business logic, no crypto."""


def calculate_total_31269(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31269():
    return 'module 31269 handles orders and invoices'
