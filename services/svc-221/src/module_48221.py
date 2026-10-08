"""Service module 48221: business logic, no crypto."""


def calculate_total_48221(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48221():
    return 'module 48221 handles orders and invoices'
