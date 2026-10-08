"""Service module 14121: business logic, no crypto."""


def calculate_total_14121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14121():
    return 'module 14121 handles orders and invoices'
