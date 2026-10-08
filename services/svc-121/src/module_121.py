"""Service module 121: business logic, no crypto."""


def calculate_total_121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_121():
    return 'module 121 handles orders and invoices'
