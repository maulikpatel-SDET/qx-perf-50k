"""Service module 17944: business logic, no crypto."""


def calculate_total_17944(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17944():
    return 'module 17944 handles orders and invoices'
