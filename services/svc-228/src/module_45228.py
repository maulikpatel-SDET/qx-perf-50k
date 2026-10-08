"""Service module 45228: business logic, no crypto."""


def calculate_total_45228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45228():
    return 'module 45228 handles orders and invoices'
