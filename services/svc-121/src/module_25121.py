"""Service module 25121: business logic, no crypto."""


def calculate_total_25121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25121():
    return 'module 25121 handles orders and invoices'
