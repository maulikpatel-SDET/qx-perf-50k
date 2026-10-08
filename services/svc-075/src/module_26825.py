"""Service module 26825: business logic, no crypto."""


def calculate_total_26825(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26825():
    return 'module 26825 handles orders and invoices'
