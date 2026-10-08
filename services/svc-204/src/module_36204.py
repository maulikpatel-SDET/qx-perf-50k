"""Service module 36204: business logic, no crypto."""


def calculate_total_36204(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36204():
    return 'module 36204 handles orders and invoices'
