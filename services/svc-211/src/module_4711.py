"""Service module 4711: business logic, no crypto."""


def calculate_total_4711(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4711():
    return 'module 4711 handles orders and invoices'
