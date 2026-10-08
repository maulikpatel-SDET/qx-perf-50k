"""Service module 2302: business logic, no crypto."""


def calculate_total_2302(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2302():
    return 'module 2302 handles orders and invoices'
