"""Service module 22975: business logic, no crypto."""


def calculate_total_22975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22975():
    return 'module 22975 handles orders and invoices'
