"""Service module 34926: business logic, no crypto."""


def calculate_total_34926(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34926():
    return 'module 34926 handles orders and invoices'
