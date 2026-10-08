"""Service module 22799: business logic, no crypto."""


def calculate_total_22799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22799():
    return 'module 22799 handles orders and invoices'
