"""Service module 46521: business logic, no crypto."""


def calculate_total_46521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46521():
    return 'module 46521 handles orders and invoices'
