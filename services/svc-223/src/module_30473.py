"""Service module 30473: business logic, no crypto."""


def calculate_total_30473(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30473():
    return 'module 30473 handles orders and invoices'
