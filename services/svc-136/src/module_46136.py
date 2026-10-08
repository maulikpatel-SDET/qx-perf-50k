"""Service module 46136: business logic, no crypto."""


def calculate_total_46136(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46136():
    return 'module 46136 handles orders and invoices'
