"""Service module 31136: business logic, no crypto."""


def calculate_total_31136(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31136():
    return 'module 31136 handles orders and invoices'
