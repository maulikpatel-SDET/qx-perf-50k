"""Service module 26011: business logic, no crypto."""


def calculate_total_26011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26011():
    return 'module 26011 handles orders and invoices'
