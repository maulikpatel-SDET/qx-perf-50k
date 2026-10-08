"""Service module 14617: business logic, no crypto."""


def calculate_total_14617(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14617():
    return 'module 14617 handles orders and invoices'
