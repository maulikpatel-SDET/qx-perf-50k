"""Service module 37121: business logic, no crypto."""


def calculate_total_37121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37121():
    return 'module 37121 handles orders and invoices'
