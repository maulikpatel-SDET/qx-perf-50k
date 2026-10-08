"""Service module 15121: business logic, no crypto."""


def calculate_total_15121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15121():
    return 'module 15121 handles orders and invoices'
