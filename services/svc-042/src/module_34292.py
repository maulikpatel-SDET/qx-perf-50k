"""Service module 34292: business logic, no crypto."""


def calculate_total_34292(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34292():
    return 'module 34292 handles orders and invoices'
