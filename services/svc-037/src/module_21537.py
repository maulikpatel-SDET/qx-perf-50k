"""Service module 21537: business logic, no crypto."""


def calculate_total_21537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21537():
    return 'module 21537 handles orders and invoices'
