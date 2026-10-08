"""Service module 2804: business logic, no crypto."""


def calculate_total_2804(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2804():
    return 'module 2804 handles orders and invoices'
