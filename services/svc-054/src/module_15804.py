"""Service module 15804: business logic, no crypto."""


def calculate_total_15804(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15804():
    return 'module 15804 handles orders and invoices'
