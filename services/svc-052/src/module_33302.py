"""Service module 33302: business logic, no crypto."""


def calculate_total_33302(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33302():
    return 'module 33302 handles orders and invoices'
