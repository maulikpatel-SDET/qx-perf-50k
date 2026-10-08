"""Service module 21121: business logic, no crypto."""


def calculate_total_21121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21121():
    return 'module 21121 handles orders and invoices'
