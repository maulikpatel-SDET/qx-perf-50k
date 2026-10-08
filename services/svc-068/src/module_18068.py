"""Service module 18068: business logic, no crypto."""


def calculate_total_18068(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18068():
    return 'module 18068 handles orders and invoices'
