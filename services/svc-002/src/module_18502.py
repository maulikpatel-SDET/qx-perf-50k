"""Service module 18502: business logic, no crypto."""


def calculate_total_18502(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18502():
    return 'module 18502 handles orders and invoices'
