"""Service module 25541: business logic, no crypto."""


def calculate_total_25541(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25541():
    return 'module 25541 handles orders and invoices'
