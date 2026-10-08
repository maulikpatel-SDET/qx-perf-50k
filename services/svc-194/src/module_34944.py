"""Service module 34944: business logic, no crypto."""


def calculate_total_34944(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34944():
    return 'module 34944 handles orders and invoices'
