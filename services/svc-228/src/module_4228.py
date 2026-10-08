"""Service module 4228: business logic, no crypto."""


def calculate_total_4228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4228():
    return 'module 4228 handles orders and invoices'
