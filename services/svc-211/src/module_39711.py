"""Service module 39711: business logic, no crypto."""


def calculate_total_39711(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39711():
    return 'module 39711 handles orders and invoices'
