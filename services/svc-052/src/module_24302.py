"""Service module 24302: business logic, no crypto."""


def calculate_total_24302(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24302():
    return 'module 24302 handles orders and invoices'
