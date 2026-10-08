"""Service module 44804: business logic, no crypto."""


def calculate_total_44804(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44804():
    return 'module 44804 handles orders and invoices'
