"""Service module 40502: business logic, no crypto."""


def calculate_total_40502(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40502():
    return 'module 40502 handles orders and invoices'
