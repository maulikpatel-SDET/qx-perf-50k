"""Service module 22205: business logic, no crypto."""


def calculate_total_22205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22205():
    return 'module 22205 handles orders and invoices'
