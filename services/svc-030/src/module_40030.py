"""Service module 40030: business logic, no crypto."""


def calculate_total_40030(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40030():
    return 'module 40030 handles orders and invoices'
