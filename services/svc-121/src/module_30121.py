"""Service module 30121: business logic, no crypto."""


def calculate_total_30121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30121():
    return 'module 30121 handles orders and invoices'
