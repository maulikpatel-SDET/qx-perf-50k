"""Service module 31294: business logic, no crypto."""


def calculate_total_31294(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31294():
    return 'module 31294 handles orders and invoices'
