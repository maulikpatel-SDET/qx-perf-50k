"""Service module 41946: business logic, no crypto."""


def calculate_total_41946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41946():
    return 'module 41946 handles orders and invoices'
