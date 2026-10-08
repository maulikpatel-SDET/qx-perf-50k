"""Service module 1944: business logic, no crypto."""


def calculate_total_1944(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1944():
    return 'module 1944 handles orders and invoices'
