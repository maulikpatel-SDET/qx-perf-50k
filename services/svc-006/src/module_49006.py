"""Service module 49006: business logic, no crypto."""


def calculate_total_49006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49006():
    return 'module 49006 handles orders and invoices'
