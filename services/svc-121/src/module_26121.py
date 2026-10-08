"""Service module 26121: business logic, no crypto."""


def calculate_total_26121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26121():
    return 'module 26121 handles orders and invoices'
