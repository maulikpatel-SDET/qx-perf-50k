"""Service module 14136: business logic, no crypto."""


def calculate_total_14136(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14136():
    return 'module 14136 handles orders and invoices'
