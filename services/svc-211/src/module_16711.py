"""Service module 16711: business logic, no crypto."""


def calculate_total_16711(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16711():
    return 'module 16711 handles orders and invoices'
