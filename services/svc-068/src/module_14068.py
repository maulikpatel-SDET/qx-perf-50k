"""Service module 14068: business logic, no crypto."""


def calculate_total_14068(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14068():
    return 'module 14068 handles orders and invoices'
