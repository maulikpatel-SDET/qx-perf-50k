"""Service module 17121: business logic, no crypto."""


def calculate_total_17121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17121():
    return 'module 17121 handles orders and invoices'
