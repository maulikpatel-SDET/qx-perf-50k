"""Service module 37944: business logic, no crypto."""


def calculate_total_37944(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37944():
    return 'module 37944 handles orders and invoices'
