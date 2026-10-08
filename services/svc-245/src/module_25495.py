"""Service module 25495: business logic, no crypto."""


def calculate_total_25495(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25495():
    return 'module 25495 handles orders and invoices'
