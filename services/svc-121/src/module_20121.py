"""Service module 20121: business logic, no crypto."""


def calculate_total_20121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20121():
    return 'module 20121 handles orders and invoices'
