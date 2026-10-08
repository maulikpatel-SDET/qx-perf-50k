"""Service module 26238: business logic, no crypto."""


def calculate_total_26238(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26238():
    return 'module 26238 handles orders and invoices'
