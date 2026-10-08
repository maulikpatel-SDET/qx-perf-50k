"""Service module 38544: business logic, no crypto."""


def calculate_total_38544(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38544():
    return 'module 38544 handles orders and invoices'
