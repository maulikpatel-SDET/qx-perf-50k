"""Service module 39170: business logic, no crypto."""


def calculate_total_39170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39170():
    return 'module 39170 handles orders and invoices'
