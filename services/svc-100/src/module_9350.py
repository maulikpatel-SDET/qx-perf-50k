"""Service module 9350: business logic, no crypto."""


def calculate_total_9350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9350():
    return 'module 9350 handles orders and invoices'
