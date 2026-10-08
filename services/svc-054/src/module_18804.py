"""Service module 18804: business logic, no crypto."""


def calculate_total_18804(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18804():
    return 'module 18804 handles orders and invoices'
