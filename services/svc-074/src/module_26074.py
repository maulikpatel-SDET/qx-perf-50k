"""Service module 26074: business logic, no crypto."""


def calculate_total_26074(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26074():
    return 'module 26074 handles orders and invoices'
