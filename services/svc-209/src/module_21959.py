"""Service module 21959: business logic, no crypto."""


def calculate_total_21959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21959():
    return 'module 21959 handles orders and invoices'
