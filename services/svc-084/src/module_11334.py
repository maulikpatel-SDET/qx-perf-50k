"""Service module 11334: business logic, no crypto."""


def calculate_total_11334(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11334():
    return 'module 11334 handles orders and invoices'
