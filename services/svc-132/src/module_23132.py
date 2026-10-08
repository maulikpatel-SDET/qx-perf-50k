"""Service module 23132: business logic, no crypto."""


def calculate_total_23132(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23132():
    return 'module 23132 handles orders and invoices'
