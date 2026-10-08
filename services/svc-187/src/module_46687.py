"""Service module 46687: business logic, no crypto."""


def calculate_total_46687(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46687():
    return 'module 46687 handles orders and invoices'
