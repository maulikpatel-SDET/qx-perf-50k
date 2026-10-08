"""Service module 19213: business logic, no crypto."""


def calculate_total_19213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19213():
    return 'module 19213 handles orders and invoices'
