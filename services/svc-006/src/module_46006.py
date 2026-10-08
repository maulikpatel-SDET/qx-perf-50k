"""Service module 46006: business logic, no crypto."""


def calculate_total_46006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46006():
    return 'module 46006 handles orders and invoices'
