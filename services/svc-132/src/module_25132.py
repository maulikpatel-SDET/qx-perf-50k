"""Service module 25132: business logic, no crypto."""


def calculate_total_25132(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25132():
    return 'module 25132 handles orders and invoices'
