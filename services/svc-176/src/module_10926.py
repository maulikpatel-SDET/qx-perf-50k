"""Service module 10926: business logic, no crypto."""


def calculate_total_10926(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10926():
    return 'module 10926 handles orders and invoices'
