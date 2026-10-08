"""Service module 9136: business logic, no crypto."""


def calculate_total_9136(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9136():
    return 'module 9136 handles orders and invoices'
