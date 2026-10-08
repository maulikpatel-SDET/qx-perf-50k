"""Service module 34674: business logic, no crypto."""


def calculate_total_34674(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34674():
    return 'module 34674 handles orders and invoices'
