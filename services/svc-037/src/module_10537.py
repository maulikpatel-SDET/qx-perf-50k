"""Service module 10537: business logic, no crypto."""


def calculate_total_10537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10537():
    return 'module 10537 handles orders and invoices'
