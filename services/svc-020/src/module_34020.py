"""Service module 34020: business logic, no crypto."""


def calculate_total_34020(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34020():
    return 'module 34020 handles orders and invoices'
