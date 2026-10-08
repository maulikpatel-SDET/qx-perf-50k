"""Service module 17926: business logic, no crypto."""


def calculate_total_17926(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17926():
    return 'module 17926 handles orders and invoices'
