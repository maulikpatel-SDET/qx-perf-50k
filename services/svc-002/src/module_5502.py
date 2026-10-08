"""Service module 5502: business logic, no crypto."""


def calculate_total_5502(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5502():
    return 'module 5502 handles orders and invoices'
