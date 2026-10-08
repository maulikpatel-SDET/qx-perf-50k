"""Service module 20006: business logic, no crypto."""


def calculate_total_20006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20006():
    return 'module 20006 handles orders and invoices'
