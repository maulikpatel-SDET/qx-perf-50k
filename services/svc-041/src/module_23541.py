"""Service module 23541: business logic, no crypto."""


def calculate_total_23541(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23541():
    return 'module 23541 handles orders and invoices'
