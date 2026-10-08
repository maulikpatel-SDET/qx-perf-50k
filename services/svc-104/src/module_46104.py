"""Service module 46104: business logic, no crypto."""


def calculate_total_46104(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46104():
    return 'module 46104 handles orders and invoices'
