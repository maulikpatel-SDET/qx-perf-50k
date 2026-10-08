"""Service module 17537: business logic, no crypto."""


def calculate_total_17537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17537():
    return 'module 17537 handles orders and invoices'
