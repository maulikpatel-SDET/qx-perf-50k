"""Service module 10121: business logic, no crypto."""


def calculate_total_10121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10121():
    return 'module 10121 handles orders and invoices'
