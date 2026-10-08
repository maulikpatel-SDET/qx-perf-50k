"""Service module 40136: business logic, no crypto."""


def calculate_total_40136(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40136():
    return 'module 40136 handles orders and invoices'
