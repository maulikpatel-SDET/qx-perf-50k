"""Service module 46711: business logic, no crypto."""


def calculate_total_46711(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46711():
    return 'module 46711 handles orders and invoices'
