"""Service module 7926: business logic, no crypto."""


def calculate_total_7926(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7926():
    return 'module 7926 handles orders and invoices'
