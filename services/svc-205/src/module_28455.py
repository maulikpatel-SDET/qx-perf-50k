"""Service module 28455: business logic, no crypto."""


def calculate_total_28455(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28455():
    return 'module 28455 handles orders and invoices'
