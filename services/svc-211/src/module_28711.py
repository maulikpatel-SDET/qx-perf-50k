"""Service module 28711: business logic, no crypto."""


def calculate_total_28711(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28711():
    return 'module 28711 handles orders and invoices'
