"""Service module 38436: business logic, no crypto."""


def calculate_total_38436(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38436():
    return 'module 38436 handles orders and invoices'
