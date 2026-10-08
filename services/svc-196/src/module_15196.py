"""Service module 15196: business logic, no crypto."""


def calculate_total_15196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15196():
    return 'module 15196 handles orders and invoices'
