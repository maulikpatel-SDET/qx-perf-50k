"""Service module 37804: business logic, no crypto."""


def calculate_total_37804(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37804():
    return 'module 37804 handles orders and invoices'
