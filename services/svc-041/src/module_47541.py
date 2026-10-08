"""Service module 47541: business logic, no crypto."""


def calculate_total_47541(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47541():
    return 'module 47541 handles orders and invoices'
