"""Service module 7804: business logic, no crypto."""


def calculate_total_7804(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7804():
    return 'module 7804 handles orders and invoices'
