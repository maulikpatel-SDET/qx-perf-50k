"""Service module 17302: business logic, no crypto."""


def calculate_total_17302(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17302():
    return 'module 17302 handles orders and invoices'
