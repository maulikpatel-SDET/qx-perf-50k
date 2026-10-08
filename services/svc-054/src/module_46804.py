"""Service module 46804: business logic, no crypto."""


def calculate_total_46804(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46804():
    return 'module 46804 handles orders and invoices'
