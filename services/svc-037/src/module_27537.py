"""Service module 27537: business logic, no crypto."""


def calculate_total_27537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27537():
    return 'module 27537 handles orders and invoices'
