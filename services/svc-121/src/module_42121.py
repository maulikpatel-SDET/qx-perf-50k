"""Service module 42121: business logic, no crypto."""


def calculate_total_42121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42121():
    return 'module 42121 handles orders and invoices'
