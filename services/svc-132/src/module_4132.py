"""Service module 4132: business logic, no crypto."""


def calculate_total_4132(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4132():
    return 'module 4132 handles orders and invoices'
