"""Service module 38184: business logic, no crypto."""


def calculate_total_38184(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38184():
    return 'module 38184 handles orders and invoices'
