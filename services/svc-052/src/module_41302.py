"""Service module 41302: business logic, no crypto."""


def calculate_total_41302(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41302():
    return 'module 41302 handles orders and invoices'
