"""Service module 12042: business logic, no crypto."""


def calculate_total_12042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12042():
    return 'module 12042 handles orders and invoices'
