"""Service module 34037: business logic, no crypto."""


def calculate_total_34037(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34037():
    return 'module 34037 handles orders and invoices'
