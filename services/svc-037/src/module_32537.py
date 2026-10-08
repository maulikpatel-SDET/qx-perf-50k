"""Service module 32537: business logic, no crypto."""


def calculate_total_32537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32537():
    return 'module 32537 handles orders and invoices'
