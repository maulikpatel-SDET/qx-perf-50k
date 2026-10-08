"""Service module 42804: business logic, no crypto."""


def calculate_total_42804(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42804():
    return 'module 42804 handles orders and invoices'
