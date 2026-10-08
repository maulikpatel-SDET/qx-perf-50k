"""Service module 5121: business logic, no crypto."""


def calculate_total_5121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5121():
    return 'module 5121 handles orders and invoices'
