"""Service module 926: business logic, no crypto."""


def calculate_total_926(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_926():
    return 'module 926 handles orders and invoices'
