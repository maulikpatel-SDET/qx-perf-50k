"""Service module 49121: business logic, no crypto."""


def calculate_total_49121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49121():
    return 'module 49121 handles orders and invoices'
