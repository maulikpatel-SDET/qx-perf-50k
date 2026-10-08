"""Service module 37537: business logic, no crypto."""


def calculate_total_37537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37537():
    return 'module 37537 handles orders and invoices'
