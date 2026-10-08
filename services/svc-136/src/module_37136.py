"""Service module 37136: business logic, no crypto."""


def calculate_total_37136(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37136():
    return 'module 37136 handles orders and invoices'
