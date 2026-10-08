"""Service module 27292: business logic, no crypto."""


def calculate_total_27292(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27292():
    return 'module 27292 handles orders and invoices'
