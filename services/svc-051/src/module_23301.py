"""Service module 23301: business logic, no crypto."""


def calculate_total_23301(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23301():
    return 'module 23301 handles orders and invoices'
