"""Service module 18136: business logic, no crypto."""


def calculate_total_18136(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18136():
    return 'module 18136 handles orders and invoices'
