"""Service module 33537: business logic, no crypto."""


def calculate_total_33537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33537():
    return 'module 33537 handles orders and invoices'
