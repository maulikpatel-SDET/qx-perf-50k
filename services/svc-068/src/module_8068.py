"""Service module 8068: business logic, no crypto."""


def calculate_total_8068(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8068():
    return 'module 8068 handles orders and invoices'
