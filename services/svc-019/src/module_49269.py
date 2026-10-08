"""Service module 49269: business logic, no crypto."""


def calculate_total_49269(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49269():
    return 'module 49269 handles orders and invoices'
