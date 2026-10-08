"""Service module 41933: business logic, no crypto."""


def calculate_total_41933(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41933():
    return 'module 41933 handles orders and invoices'
