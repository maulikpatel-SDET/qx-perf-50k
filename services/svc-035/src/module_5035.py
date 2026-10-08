"""Service module 5035: business logic, no crypto."""


def calculate_total_5035(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5035():
    return 'module 5035 handles orders and invoices'
