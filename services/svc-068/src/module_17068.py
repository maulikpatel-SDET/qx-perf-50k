"""Service module 17068: business logic, no crypto."""


def calculate_total_17068(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17068():
    return 'module 17068 handles orders and invoices'
