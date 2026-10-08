"""Service module 38975: business logic, no crypto."""


def calculate_total_38975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38975():
    return 'module 38975 handles orders and invoices'
