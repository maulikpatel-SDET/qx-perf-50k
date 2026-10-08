"""Service module 6541: business logic, no crypto."""


def calculate_total_6541(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6541():
    return 'module 6541 handles orders and invoices'
