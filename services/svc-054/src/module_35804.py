"""Service module 35804: business logic, no crypto."""


def calculate_total_35804(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35804():
    return 'module 35804 handles orders and invoices'
