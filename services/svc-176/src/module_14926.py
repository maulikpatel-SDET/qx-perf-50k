"""Service module 14926: business logic, no crypto."""


def calculate_total_14926(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14926():
    return 'module 14926 handles orders and invoices'
